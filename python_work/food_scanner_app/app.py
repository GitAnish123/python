import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
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

# Sidebar instructions
st.sidebar.title("🍽 Food Scanner Instructions")
st.sidebar.write("""
1. Choose input method: take a photo or upload one.
2. The app will predict what the food is.
3. Nutrition info will appear for the top prediction.
4. Add this app to your home screen for a full mobile experience.
""")

# -------------------------------
# App Title
# -------------------------------
st.markdown("<h1 style='text-align: center;'>🍎 Food Scanner App</h1>", unsafe_allow_html=True)
st.markdown("---")

# -------------------------------
# Load Food-101 Model (Best Accuracy)
# -------------------------------
@st.cache_resource
def load_model():
    model = hub.load("https://tfhub.dev/google/food_classifier_mobilenet_v2_1.0_224/1")
    return model

model = load_model()

# Load Food-101 labels
LABELS_URL = "https://raw.githubusercontent.com/tensorflow/models/master/research/slim/datasets/food101_labels.txt"
labels = requests.get(LABELS_URL).text.strip().split("\n")

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
# Input Method Toggle
# -------------------------------
input_method = st.radio("Choose input method:", ["Camera", "Upload Photo"])

if input_method == "Camera":
    uploaded_file = st.camera_input("Take a photo of your food")
else:
    uploaded_file = st.file_uploader("Upload a photo of your food", type=["jpg","jpeg","png"])

# -------------------------------
# Process Image if Provided
# -------------------------------
if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Selected Image", use_column_width=True)
    st.write("🔍 Analyzing image...")

    # Preprocess for Food-101 model
    img_resized = img.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    preds = model(img_array)
    top_indices = tf.argsort(preds, direction='DESCENDING')[0][:3].numpy()
    confidences = tf.nn.softmax(preds[0]).numpy()

    st.markdown("## 🔍 Top Predictions")
    for i, idx in enumerate(top_indices):
        label = labels[idx].replace("_", " ").title()
        confidence = confidences[idx] * 100
        st.write(f"{i+1}. {label} ({confidence:.2f}%)")

    # Nutrition Info
    top_guess = labels[top_indices[0]].replace("_", " ")
    st.markdown("## 🥗 Nutrition Info")
    food_info = search_usda(top_guess)

    if food_info:
        st.write("**Item:**", food_info.get("description", "Unknown"))
        nutrients = food_info.get("foodNutrients", [])
        if nutrients:
            data = []
            for n in nutrients[:15]:
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
    st.write("👆 Please take a photo or upload an image first.")