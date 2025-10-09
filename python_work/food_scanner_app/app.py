import streamlit as st
from PIL import Image
import numpy as np
from keras.applications import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from keras.utils import img_to_array
import pandas as pd
import requests

# -------------------------------
# App Configuration
# -------------------------------
st.set_page_config(
    page_title="🍎 Food Scanner App",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("🍽 Food Scanner Instructions")
st.sidebar.write("""
1. Choose input method: take a photo or upload one.
2. The app will predict what the food is.
3. Nutrition info will appear for the top prediction.
4. Add this app to your home screen for a full mobile experience.
""")

st.markdown("<h1 style='text-align: center;'>🍎 Food Scanner App</h1>", unsafe_allow_html=True)
st.markdown("---")

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    return MobileNetV2(weights="imagenet")

model = load_model()

# -------------------------------
# USDA API Key & Function
# -------------------------------
API_KEY = "WPJ29FiN6XjLhX1VljTsAfpRVzl4aa8gTuOWDmrU"

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
# Input Method
# -------------------------------
input_method = st.radio("Choose input method:", ["Camera", "Upload Photo"])
if input_method == "Camera":
    uploaded_file = st.camera_input("Take a photo of your food")
else:
    uploaded_file = st.file_uploader("Upload a photo of your food", type=["jpg","jpeg","png"])

# -------------------------------
# Process Image
# -------------------------------
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Selected Image", use_column_width=True)
    st.write("🔍 Analyzing image...")

    img_resized = img.resize((224, 224))
    x = img_to_array(img_resized)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    decoded = decode_predictions(preds, top=5)[0]

    # Simple mapping to common foods to improve accuracy
    food_labels = ["pizza","hamburger","hotdog","ice_cream","donut","cake","spaghetti","sushi","salad","banana","apple","orange","sandwich"]
    top_food = next((d[1].replace("_"," ") for d in decoded if d[1].replace("_"," ") in food_labels), decoded[0][1].replace("_"," "))

    st.markdown("## 🔍 Top Predictions")
    for i, d in enumerate(decoded[:3], start=1):
        st.write(f"{i}. {d[1].replace('_',' ').title()} ({d[2]*100:.2f}%)")

    st.markdown("## 🥗 Nutrition Info")
    food_info = search_usda(top_food)
    if food_info:
        st.write("**Item:**", food_info.get("description","Unknown"))
        nutrients = food_info.get("foodNutrients", [])
        if nutrients:
            data=[]
            for n in nutrients[:15]:
                data.append([n.get("nutrientName",""), n.get("value",""), n.get("unitName","")])
            df = pd.DataFrame(data, columns=["Nutrient","Amount","Unit"])
            st.dataframe(df,use_container_width=True)
        else:
            st.write("No nutrient info found.")
    else:
        st.warning("No nutrition data found. Try a more specific food name.")
else:
    st.write("👆 Please take a photo or upload an image first.")