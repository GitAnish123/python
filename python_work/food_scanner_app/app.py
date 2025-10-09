import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import requests
import torch
import clip

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
# Load CLIP Model
# -------------------------------
@st.cache_resource
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device=device)
    return model, preprocess, device

model, preprocess, device = load_model()

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
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Selected Image", use_column_width=True)
    st.write("🔍 Analyzing image...")

    # Preprocess image for CLIP
    image_input = preprocess(img).unsqueeze(0).to(device)

    # Text labels (thousands of common foods)
    # This is just a sample; you can expand the list as needed
    food_labels = [
        "pizza", "hamburger", "hot dog", "ice cream", "donut", "cake", "spaghetti",
        "sushi", "salad", "banana", "apple", "orange", "sandwich", "tacos", "pasta",
        "fried chicken", "steak", "pancakes", "waffles", "burrito", "ramen", "soup",
        "dumplings", "falafel", "chocolate", "cheese", "bagel", "croissant", "cookies"
    ]
    text_inputs = torch.cat([clip.tokenize(f) for f in food_labels]).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)
        similarity = (100.0 * image_features @ text_features.T).squeeze(0)
        values, indices = similarity.topk(5)

    st.markdown("## 🔍 Top Predictions")
    for i, idx in enumerate(indices):
        st.write(f"{i+1}. {food_labels[idx]} ({values[i]:.2f}%)")

    # -------------------------------
    # Nutrition Info
    # -------------------------------
    top_food = food_labels[indices[0]]
    st.markdown("## 🥗 Nutrition Info")
    food_info = search_usda(top_food)
    if food_info:
        st.write("**Item:**", food_info.get("description", "Unknown"))
        nutrients = food_info.get("foodNutrients", [])
        if nutrients:
            data = []
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