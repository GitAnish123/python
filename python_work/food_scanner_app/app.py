import streamlit as st
from PIL import Image
import numpy as np
from keras.applications import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from keras.utils import img_to_array
import pandas as pd
import requests

# -------------------------------
# App Title and Sidebar
# -------------------------------
st.set_page_config(page_title="🍎 Food Scanner App", layout="wide")
st.title("🍎 Food Scanner App")
st.sidebar.title("🍽 Food Scanner Instructions")
st.sidebar.write("""
1. Upload a photo of your food.
2. The app will predict what the food is.
3. Nutrition info will appear for the top prediction.
""")

# -------------------------------
# Load MobileNetV2 model
# -------------------------------
@st.cache_resource
def load_model():
    return MobileNetV2(weights="imagenet")

model = load_model()

# -------------------------------
# USDA API Key
# -------------------------------
API_KEY = "WPJ29FiN6XjLhX1VljTsAfpRVzl4aa8gTuOWDmrU"

# Function to search USDA
def search_usda(query):
    url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    params = {"api_key": API_KEY, "query": query, "pageSize": 3}
    res = requests.get(url, params=params)
    if res.status_code != 200:
        return None
    data = res.json()
    if "foods" not in data or len(data["foods"]) == 0:
        return None
    return data["foods"][0]

# -------------------------------
# Upload Section
# -------------------------------
st.markdown("## 🍏 Upload Your Food Image")
st.markdown("---")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and display image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    st.write("🔍 Analyzing image...")

    # Preprocess for MobileNetV2
    img_resized = img.resize((224, 224))
    x = img_to_array(img_resized)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # -------------------------------
    # Predictions Section
    # -------------------------------
    preds = model.predict(x)
    decoded = decode_predictions(preds, top=3)[0]

    st.markdown("## 🔍 Top Predictions")
    st.markdown("---")
    for i, pred in enumerate(decoded, start=1):
        st.write(f"{i}. {pred[1].replace('_', ' ').title()} ({pred[2]*100:.2f}%)")

    # -------------------------------
    # Nutrition Info Section
    # -------------------------------
    top_guess = decoded[0][1].replace('_', ' ')
    st.markdown("## 🥗 Nutrition Info")
    st.markdown("---")
    st.subheader(f"Nutrition Info for {top_guess.title()}:")

    food_info = search_usda(top_guess)
    if food_info:
        st.write("**Item:**", food_info.get("description", "Unknown"))

        nutrients = food_info.get("foodNutrients", [])
        if nutrients:
            # Convert to table
            data = []
            for n in nutrients[:15]:  # first 15 nutrients
                name = n.get("nutrientName", "")
                value = n.get("value", "")
                unit = n.get("unitName", "")
                data.append([name, value, unit])
            df = pd.DataFrame(data, columns=["Nutrient", "Amount", "Unit"])
            st.dataframe(df, use_container_width=True)
        else:
            st.write("No nutrient info found.")
    else:
        st.warning("No nutrition data found. Try a more specific food name.")

else:
    st.write("👆 Please upload an image first.")