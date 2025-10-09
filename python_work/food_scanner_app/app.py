import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd
import requests

# ---------------------------------
# Streamlit App Config
# ---------------------------------
st.set_page_config(
    page_title="🍎 Food Scanner App",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("🍽 Food Scanner Instructions")
st.sidebar.write("""
1. Use your camera or upload a food image.
2. The app will identify the food using a trained Food-101 model.
3. Nutrition info will appear for the top result.
""")

st.markdown("<h1 style='text-align:center;'>🍱 Food Scanner App</h1>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------
# Load Food-101 Model
# ---------------------------------
@st.cache_resource
def load_food_model():
    model = hub.load("https://tfhub.dev/google/food_classifier_mobilenet_v2_1.0_224/1")
    return model

model = load_food_model()

# ---------------------------------
# Food-101 labels
# ---------------------------------
LABELS_URL = "https://raw.githubusercontent.com/tensorflow/models/master/research/slim/datasets/food101_labels.txt"
labels = requests.get(LABELS_URL).text.strip().split("\n")

# ---------------------------------
# USDA API Key
# ---------------------------------
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

# ---------------------------------
# Image Upload / Camera Input
# ---------------------------------
st.markdown("## 📸 Capture or Upload Your Food Image")
uploaded_file = st.camera_input("Take a photo") or st.file_uploader("...or upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load image
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Your Image", use_column_width=True)
    st.write("🔍 Analyzing...")

    # Preprocess for model
    img_resized = img.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict food class
    preds = model(img_array)
    pred_idx = tf.argmax(preds, axis=-1).numpy()[0]
    confidence = tf.reduce_max(preds, axis=-1).numpy()[0]
    food_name = labels[pred_idx].replace("_", " ").title()

    # ---------------------------------
    # Display results
    # ---------------------------------
    st.markdown(f"### 🍔 Predicted Food: **{food_name}** ({confidence*100:.2f}%)")

    # Nutrition info
    st.markdown("## 🥗 Nutrition Info")
    food_info = search_usda(food_name)

    if food_info:
        st.write("**Item:**", food_info.get("description", "Unknown"))
        nutrients = food_info.get("foodNutrients", [])
        if nutrients:
            data = []
            for n in nutrients[:15]:
                data.append([
                    n.get("nutrientName", ""),
                    n.get("value", ""),
                    n.get("unitName", "")
                ])
            df = pd.DataFrame(data, columns=["Nutrient", "Amount", "Unit"])
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No nutrient info found.")
    else:
        st.warning("No nutrition data found. Try a more common food name.")

else:
    st.info("👆 Please take or upload a photo to start.")