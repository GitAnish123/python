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
    'pizza', 'hamburger', 'hot dog', 'ice cream', 'donut', 'cake', 'spaghetti', 'salad',
    'banana bread', 'apple pie', 'sandwich', 'pasta', 'fried chicken', 'steak', 'pancakes',
    'waffles', 'soup', 'chocolate', 'cheese', 'bagel', 'cookies', 'mac and cheese',
    'lasagna', 'carbonara', 'bolognese', 'alfredo pasta', 'grilled cheese', 'fish and chips',
    'mashed potatoes', 'roast beef', 'beef wellington', 'yorkshire pudding',
    'brownies', 'cupcakes', 'muffins', 'bread pudding', 'milkshake', 'smoothie', 'coffee',
    'tea', 'iced tea', 'lemonade', 'soda', 'cola', 'root beer', 'eggs', 'toast', 'cereal',
    'bacon', 'sausage', 'omelette', 'scrambled eggs', 'fried eggs', 'buttered toast',
    'peanut butter sandwich', 'grilled chicken', 'roast chicken', 'baked potato', 'cornbread',
    'biscuits', 'pasta salad', 'fruit salad', 'coleslaw', 'potato salad', 'vegetable soup',
    'chicken soup', 'tomato soup', 'pumpkin soup', 'bread roll', 'pudding', 'ice cream sundae',
    'milk', 'butter', 'yogurt', 'jam', 'honey', 'oats', 'toast with jam',
    'biryani', 'chicken biryani', 'mutton biryani', 'vegetable biryani', 'rogan josh',
    'korma', 'butter chicken', 'chicken tikka masala', 'chicken tikka', 'paneer tikka',
    'paneer butter masala', 'dal makhani', 'dal fry', 'dal tadka', 'chole bhature',
    'chole masala', 'rajma masala', 'aloo gobi', 'bhindi masala', 'saag paneer', 'palak paneer',
    'malai kofta', 'kofta', 'vindaloo', 'lamb curry', 'fish curry', 'egg curry', 'prawn curry',
    'tandoori chicken', 'naan', 'butter naan', 'garlic naan', 'roti', 'chapati', 'paratha',
    'lachha paratha', 'rumali roti', 'puri', 'bhature', 'kulcha', 'pav', 'pav bhaji', 'vada pav',
    'misal pav', 'poha', 'upma', 'idli', 'dosa', 'masala dosa', 'uttapam', 'medu vada',
    'sambar', 'rasam', 'thepla', 'dhokla', 'khandvi', 'fafda', 'kachori', 'samosa', 'pakora',
    'bonda', 'pani puri', 'golgappa', 'sev puri', 'dahi puri', 'chaat', 'masala peanuts',
    'pulao', 'jeera rice', 'fried rice veg', 'paneer manchurian', 'bread pakora',
    'grilled sandwich', 'cheese sandwich', 'burger veg', 'burger chicken', 'chai',
    'masala chai', 'ginger chai', 'lassi', 'mango lassi', 'sweet lassi', 'falooda', 'kulfi',
    'gulab jamun', 'rasgulla', 'jalebi', 'barfi', 'kaju katli', 'peda', 'modak', 'ladoos',
    'besan ladoo', 'motichoor ladoo', 'soan papdi', 'imarti', 'basundi', 'rabri', 'phirni',
    'kheer', 'shrikhand', 'puran poli', 'dal bati churma', 'halwa', 'suji halwa', 'gajar halwa',
    'payasam', 'mango juice', 'coconut water', 'pomegranate juice', 'curd', 'raita',
    'boondi raita', 'cucumber raita', 'papad', 'pickle', 'achar', 'onion salad',
    'apple', 'banana', 'orange', 'grape', 'pear', 'peach', 'plum', 'cherry', 'strawberry',
    'blueberry', 'raspberry', 'blackberry', 'watermelon', 'cantaloupe', 'honeydew',
    'pineapple', 'mango', 'papaya', 'guava', 'kiwi', 'lemon', 'lime', 'pomegranate',
    'coconut', 'fig', 'date', 'apricot', 'tangerine', 'nectarine', 'cranberry', 'dragon fruit',
    'passion fruit', 'jackfruit', 'lychee', 'star fruit', 'mulberry', 'custard apple', 'sapota',
    'berries', 'avocado', 'grapefruit', 'potato', 'sweet potato', 'carrot', 'onion', 'tomato', 'garlic', 
    'ginger', 'cucumber', 'spinach', 'lettuce', 'cabbage', 'cauliflower', 'broccoli', 'peas', 'green beans',
    'bell pepper', 'capsicum', 'chili pepper', 'corn', 'eggplant', 'brinjal', 'okra', 'ladyfinger',
    'pumpkin', 'zucchini', 'radish', 'beetroot', 'turnip', 'celery', 'leek', 'asparagus',
    'artichoke', 'mushroom', 'kale', 'mustard greens', 'fenugreek leaves', 'drumstick',
    'bottle gourd', 'ridge gourd', 'bitter gourd', 'coriander', 'mint', 'parsley', 'basil',
    'spring onion', 'curry leaves', 'almond', 'cashew', 'peanut', 'walnut', 'pistachio', 'hazelnut', 'pecan', 
    'macadamia', 'brazil nut', 'pine nut', 'chestnut', 'sunflower seed', 'pumpkin seed', 'chia seed',
    'flaxseed', 'sesame seed', 'melon seed', 'coconut meat', 'groundnut'
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