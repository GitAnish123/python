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
    "pizza", "hamburger", "hot dog", "ice cream", "donut", "cake", "spaghetti", "sushi", "salad", "banana",
    "apple", "orange", "sandwich", "tacos", "pasta", "fried chicken", "steak", "pancakes", "waffles", "burrito",
    "ramen", "soup", "dumplings", "falafel", "chocolate", "cheese", "bagel", "croissant", "cookies", "fried rice",
    "sushi roll", "curry", "sashimi", "tempura", "ramen noodles", "bento box", "sashimi platter", "teriyaki chicken",
    "sushi nigiri", "yakitori", "miso soup", "udon noodles", "tonkatsu", "gyoza", "takoyaki", "onigiri", "okonomiyaki",
    "chashu pork", "nigiri sushi", "sushi maki", "sushi temaki", "sushi chirashi", "sushi donburi", "sushi platter",
    "sushi bento", "sushi box", "sushi rolls", "sushi sashimi", "sushi sashimi platter", "soba noodles", "pho",
    "pad thai", "green curry", "red curry", "massaman curry", "yellow curry", "panang curry", "tom yum soup",
    "tom kha soup", "laksa", "beef stew", "chili", "lasagna", "carbonara", "bolognese", "alfredo pasta",
    "mac and cheese", "gnocchi", "polenta", "risotto", "paella", "tortilla soup", "ceviche", "fish tacos",
    "crab cakes", "clam chowder", "lobster bisque", "seafood paella", "shrimp scampi", "grilled salmon",
    "grilled tuna", "grilled tilapia", "grilled trout", "grilled shrimp", "grilled scallops", "oysters Rockefeller",
    "mussels marinara", "octopus salad", "calamari fritti", "squid ink pasta", "stuffed peppers", "stuffed mushrooms",
    "bruschetta", "caprese salad", "caesar salad", "greek salad", "niçoise salad", "wedge salad", "coleslaw",
    "potato salad", "beet salad", "arugula salad", "kale salad", "cobb salad", "chef salad", "fruit salad",
    "antipasto", "tabbouleh", "hummus", "baba ghanoush", "falafel wrap", "shawarma", "gyros", "doner kebab",
    "chicken tikka masala", "paneer tikka", "palak paneer", "butter chicken", "dal makhani", "chole bhature",
    "samosa", "pakora", "biryani", "vegetable biryani", "chicken biryani", "mutton biryani", "lamb kebab",
    "beef kebab", "chicken kebab", "kofta", "shish kebab", "fajitas", "enchiladas", "quesadilla", "chimichanga",
    "nachos", "guacamole", "salsa", "tortilla chips", "flan", "tiramisu", "panna cotta", "gelato", "cannoli",
    "profiteroles", "éclairs", "macarons", "crepes", "churros", "soufflé", "brownies", "blondies", "cupcakes",
    "muffins", "banana bread", "zucchini bread", "pumpkin bread", "bread pudding", "sticky toffee pudding",
    "apple pie", "pecan pie", "key lime pie", "lemon meringue pie", "chocolate cake", "red velvet cake",
    "carrot cake", "cheesecake", "ice cream sundae", "banana split", "milkshake", "smoothie", "fruit smoothie",
    "protein shake", "matcha latte", "latte", "cappuccino", "espresso", "americano", "flat white", "mocha",
    "hot chocolate", "chai latte", "bubble tea", "boba tea", "kombucha", "green juice", "detox juice",
    "cocktail", "mocktail", "wine", "beer", "whiskey", "gin", "rum", "vodka", "tequila", "sangria", "margarita"
    ]
    food_labels += [
    "pizza", "hamburger", "hot dog", "ice cream", "donut", "cake", "spaghetti", "sushi", "salad", "banana",
    "apple", "orange", "sandwich", "tacos", "pasta", "fried chicken", "steak", "pancakes", "waffles", "burrito",
    "ramen", "soup", "dumplings", "falafel", "chocolate", "cheese", "bagel", "croissant", "cookies",
    "samosa", "paneer tikka", "butter chicken", "chicken biryani", "lamb curry", "masala dosa", "idli", "vada",
    "poha", "upma", "pav bhaji", "vada pav", "dal makhani", "chole bhature", "roti", "naan", "tandoori chicken",
    "fish curry", "shrimp curry", "palak paneer", "saag paneer", "egg curry", "mutton kebab", "seekh kebab",
    "chicken tikka", "pork belly", "beef stew", "clam chowder", "lobster bisque", "crab cakes", "oysters",
    "escargot", "coq au vin", "ratatouille", "bouillabaisse", "quiche", "croque madame", "croque monsieur",
    "mac and cheese", "grilled cheese", "philly cheesesteak", "cornbread", "biscuits", "gumbo", "jambalaya",
    "crawfish étouffée", "po' boy sandwich", "pulled pork sandwich", "reuben sandwich", "club sandwich",
    "BLT sandwich", "gyro", "shawarma", "falafel wrap", "hummus plate", "tabbouleh", "baba ganoush",
    "dolma", "baklava", "spanakopita", "moussaka", "tzatziki", "gyro plate", "chicken shawarma", "lamb shawarma",
    "pizza margherita", "pizza pepperoni", "pizza veggie", "pizza quattro formaggi", "pizza hawaiian",
    "calzone", "stromboli", "focaccia", "bruschetta", "caprese salad", "caesar salad", "greek salad",
    "garden salad", "coleslaw", "potato salad", "macaroni salad", "fruit salad", "chicken salad",
    "egg salad", "tuna salad", "cobb salad", "niçoise salad", "ceviche", "pasta carbonara", "pasta alfredo",
    "pasta pesto", "pasta arrabiata", "spaghetti bolognese", "spaghetti aglio e olio", "lasagna", "ravioli",
    "tortellini", "gnocchi", "fettuccine", "linguine", "tagliatelle", "penne arrabiata", "farfalle",
    "seafood paella", "chorizo paella", "arroz con pollo", "enchiladas", "tostadas", "quesadillas", "tamales",
    "chilaquiles", "mole poblano", "salsa verde chicken", "carnitas", "al pastor", "barbacoa", "pozole",
    "pho", "bun cha", "banh mi", "spring rolls", "egg rolls", "pad thai", "pad see ew", "green curry",
    "red curry", "yellow curry", "massaman curry", "tom yum soup", "tom kha soup", "sticky rice mango",
    "dim sum", "char siu", "baozi", "xiao long bao", "dan dan noodles", "mapo tofu", "kung pao chicken",
    "sweet and sour pork", "hot pot", "jajangmyeon", "bibimbap", "kimchi stew", "bulgogi", "galbi",
    "tteokbokki", "kimbap", "ramyeon", "soondubu jjigae", "samgyeopsal", "japchae", "tonkatsu",
    "katsudon", "okonomiyaki", "takoyaki", "unagi don", "chirashi sushi", "sushi nigiri", "sushi maki",
    "sashimi platter", "yakitori", "ramen noodles", "udon noodles", "tempura", "miso soup", "bento box",
    "croissant sandwich", "pain au chocolat", "eclair", "profiterole", "tarte tatin", "creme brulee",
    "panna cotta", "tiramisu", "gelato", "sorbet", "cheesecake", "brownie", "cupcake", "macaron",
    "apple pie", "pecan pie", "pumpkin pie", "key lime pie", "chocolate mousse", "chocolate lava cake",
    "banana bread", "zucchini bread", "muffin", "scone", "donut glazed", "donut chocolate", "donut jelly",
    "ice cream sundae", "milkshake", "smoothie", "bubble tea", "mocha", "latte", "cappuccino", "espresso",
    "americano", "flat white", "chai latte", "hot chocolate", "green tea", "matcha latte", "oolong tea",
    "black tea", "herbal tea", "kombucha", "lemonade", "orange juice", "apple juice", "grape juice",
    "carrot juice", "celery juice", "tomato juice", "veggie smoothie", "protein shake", "cocktail",
    "margarita", "mojito", "pina colada", "martini", "whiskey sour", "old fashioned", "gin and tonic",
    "beer", "red wine", "white wine", "rose wine", "champagne", "sparkling water", "iced tea", "soda",
    "cola", "root beer", "ginger ale", "energy drink", "sports drink", "kombu tea", "soju", "sake",
    "plum wine", "baijiu", "tequila", "rum", "vodka", "gin", "cognac", "brandy", "liqueur",
    ]
    food_labels += [
    "arancini", "bucatini all'amatriciana", "caponata", "gnocchi sorrentino", "osso buco",
    "veal scaloppine", "frittata", "branzino", "cioppino", "clam linguine", "shrimp scampi",
    "moules frites", "beef bourguignon", "duck confit", "chicken cordon bleu", "sole meuniere",
    "coquilles st jacques", "crepes suzette", "ratatouille tian", "niçoise tart", "salmon en papillote",
    "bouillabaisse marseillaise", "cassoulet", "quiche lorraine", "pissaladière", "tarte flambée",
    "flammkuchen", "bratwurst", "sauerkraut", "schweinsbraten", "kartoffelsalat", "spätzle",
    "käsespätzle", "maultaschen", "lebkuchen", "stollen", "apfelstrudel", "bienenstich", "schwarzwälder kirschtorte",
    "linzer torte", "tiramisu espresso", "pavlova", "lamington", "anpan", "melon pan", "dorayaki",
    "taiyaki", "mochi", "wagashi", "matcha cake", "red bean bun", "green tea ice cream",
    "yakisoba", "okonomiyaki seafood", "okonomiyaki pork", "takoyaki octopus", "takoyaki cheese",
    "onigiri salmon", "onigiri tuna mayo", "chirashi don", "katsudon tonkatsu", "oyakodon",
    "gyudon", "tempura udon", "kitsune udon", "zaru soba", "soba salad", "hiyashi chuka", "chawanmushi",
    "agedashi tofu", "kare raisu", "chili crab", "black pepper crab", "crab fried rice", "chilli paneer",
    "veg manchurian", "spring onion noodles", "hakka noodles", "chow mein", "lo mein",
    "sichuan hot pot", "gong bao chicken", "sweet and sour chicken", "beef chow fun", "mapo tofu",
    "dan dan noodles spicy", "hot and sour soup", "wonton soup", "egg drop soup", "fish ball soup",
    "congee", "char kway teow", "nasi goreng", "mee goreng", "satay chicken", "rendang beef",
    "laksa", "hokkien mee", "roti canai", "teh tarik", "ayam goreng", "gado gado", "babi kecap",
    "pempek", "tahu gejrot", "ayam penyet", "sate lilit", "ayam betutu", "bubur ayam", "lumpia",
    "kue lapis", "kue cubit", "kue nastar", "kue putu", "onde-onde", "es cendol", "es teler",
    "boba milk tea", "pandan cake", "durian pancake", "mango sticky rice", "thai iced tea",
    "tom kha gai", "som tam", "pad kra pao", "massaman curry chicken", "green curry beef",
    "panang curry", "yellow curry prawn", "red curry duck", "larb gai", "sticky rice mango",
    "kanom chan", "kanom krok", "kanom buang", "khao soi", "gaeng hung lay", "mee krob",
    "bak kut teh", "char siew rice", "siu yuk", "claypot chicken rice", "yu sheng", "loh bak",
    "teochew porridge", "chwee kueh", "nian gao", "baozi pork", "xiaolong bao", "sheng jian bao",
    "mantou", "jiaozi", "suan la tang", "lu rou fan", "zhajiangmian", "beef noodle soup",
    "pork belly buns", "stinky tofu", "hot dog korean", "tteokbokki spicy", "kimbap", "kimchi fried rice",
    "bibim naengmyeon", "mul naengmyeon", "soondubu jjigae", "galbitang", "samgyetang", "gamjatang",
    "dak galbi", "bulgogi beef", "spicy pork bulgogi", "japchae sweet potato", "haemul pajeon",
    "kimchi jeon", "soju cocktail", "makgeolli", "baekseju", "cheongju", "yukgaejang", "sundae korean",
    "bingsu red bean", "bingsu mango", "hotteok", "injeolmi", "chapchae", "kimchi pancake",
    "gimbap tuna", "gimbap cheese", "gimbap beef", "gimbap chicken", "mandu soup", "mandu spicy",
    "ramyeon instant", "ramyeon cheese", "ramyeon seafood", "ramyeon beef", "korean fried chicken",
    "dakgangjeong", "yangnyeom chicken", "honey soy chicken", "fried calamari", "fried shrimp",
    "fish and chips malt vinegar", "fish and chips tartar", "clam chowder bread bowl", "lobster roll",
    "new england lobster", "maine lobster", "grilled salmon teriyaki", "salmon sashimi", "tuna sashimi",
    "eel unagi", "octopus carpaccio", "shrimp tempura", "crab tempura", "crab legs garlic butter",
    "oysters rockefeller", "oysters kilpatrick", "mussels marinara", "mussels white wine", "clams casino",
    "bangers and mash", "shepherd's pie", "cornish pasty", "beef wellington", "roast beef yorkshire",
    "sticky toffee pudding", "bread and butter pudding", "trifle", "jam roly poly", "spotted dick",
    "eccles cake", "mince pie", "yorkshire pudding", "black pudding", "blood sausage", "cock-a-leekie soup",
    "haggis", "neeps and tatties", "cullen skink", "forfar bridie", "stargazy pie", "kedgeree",
    "ploughman's lunch", "scotch egg", "clootie dumpling", "leek and potato soup", "rogan josh",
    "biryani lamb", "biryani chicken", "biryani vegetarian", "korma chicken", "korma lamb",
    "vindaloo beef", "vindaloo chicken", "tikka masala chicken", "tikka masala paneer", "saag chicken",
    "saag lamb", "dal tadka", "dal fry", "rajma masala", "chana masala", "aloo gobi", "bhindi masala",
    "pav bhaji cheese", "vada pav spicy", "idli sambar", "dosa masala", "medu vada", "uttapam",
    "puli kozhukattai", "kozhukattai sweet", "poha indori", "upma semolina", "chole masala",
    "paneer butter masala", "butter naan", "garlic naan", "lachha paratha", "rumali roti",
    ]
    food_labels += [
    "naan bread", "roti", "paratha", "chapati", "puri", "bhature", "kulcha", "pav", "papadum", 
    "samosa aloo", "samosa meat", "pakora", "bhaji", "kachori", "pani puri", "golgappa", "sev puri",
    "dahi puri", "vada pav masala", "misal pav", "poori bhaji", "dal bhati churma", "petha sweet", 
    "rasgulla", "gulab jamun", "jalebi", "soan papdi", "barfi", "kaju katli", "ladoos", "modak", 
    "peda", "kalakand", "milk cake", "basundi", "rabri", "phirni", "shrikhand", "kulfi", "falooda", 
    "mango lassi", "sweet lassi", "salted lassi", "masala chai", "ginger chai", "cardamom tea", 
    "green tea", "oolong tea", "black tea", "white tea", "herbal tea", "turmeric latte", "golden milk",
    "espresso", "cappuccino", "latte", "mocha", "americano", "macchiato", "flat white", "irish coffee",
    "affogato", "chai latte", "matcha latte", "frappuccino", "iced coffee", "cold brew", "kombucha",
    "sparkling water", "mineral water", "soda cola", "lemon soda", "orange juice", "apple juice",
    "mango juice", "pineapple juice", "carrot juice", "tomato juice", "grape juice", "pomegranate juice",
    "coconut water", "smoothie banana", "smoothie strawberry", "smoothie mango", "smoothie mixed berries",
    "energy drink", "sports drink", "milkshake chocolate", "milkshake vanilla", "milkshake strawberry",
    "milkshake caramel", "protein shake", "almond milk", "soy milk", "oat milk", "rice milk", "cashew milk",
    "paneer tikka", "chicken tikka", "seekh kebab", "shami kebab", "tandoori chicken", "malai tikka",
    "chicken bhuna", "chicken do pyaza", "lamb rogan josh", "lamb korma", "beef vindaloo", "prawn masala",
    "fish curry", "pomfret fry", "mackerel curry", "crab curry", "prawn balchao", "kerala prawn curry",
    "goan fish curry", "bombil fry", "bangda fry", "sardine fry", "roasted corn", "corn chaat", "chili corn",
    "masala peanuts", "chana chaat", "rajma salad", "chickpea salad", "fruit chaat", "cucumber raita",
    "boondi raita", "pulao veg", "pulao chicken", "jeera rice", "fried rice veg", "fried rice chicken",
    "chow mein veg", "chow mein chicken", "hakka noodles veg", "hakka noodles chicken", "manchurian veg",
    "manchurian chicken", "paneer manchurian", "veg spring rolls", "chicken spring rolls", "fish fingers",
    "bread pakora", "vada sandwich", "egg sandwich", "grilled sandwich veg", "grilled sandwich chicken",
    "cheese sandwich", "club sandwich", "burger veg", "burger chicken", "burger beef", "hot dog classic",
    "hot dog cheese", "hot dog chili", "mac and cheese", "spaghetti aglio olio", "spaghetti bolognese",
    "lasagna veg", "lasagna meat", "fettuccine alfredo", "carbonara pasta", "penne arrabbiata",
    "gnocchi potato", "gnocchi spinach", "risotto mushroom", "risotto seafood", "risotto chicken",
    "mushroom soup", "tomato soup", "pumpkin soup", "cream of chicken soup", "minestrone soup",
    "vegetable soup", "chowder corn", "clam chowder", "lobster bisque", "seafood chowder", "pho beef",
    "pho chicken", "bun cha", "banh mi pork", "banh mi chicken", "spring rolls vietnamese",
    "sticky rice vietnamese", "lemongrass chicken vietnamese", "coconut curry soup", "green curry soup",
    "massaman curry soup", "pad see ew", "pad thai shrimp", "pad thai chicken", "khao pad",
    "som tam papaya", "larb chicken", "gaeng keow wan", "tom yum goong", "tom kha gai", "satay beef",
    "satay chicken", "rendang beef", "gado gado", "ayam goreng", "nasi lemak", "mee rebus",
    "laksa lemak", "hainanese chicken rice", "char kway teow", "hokkien mee", "bak kut teh", "chwee kueh",
    "nian gao", "tang yuan", "baozi pork", "xiaolong bao", "sheng jian bao", "mantou", "jiaozi pork",
    "jiaozi veggie", "wontons pork", "wontons shrimp", "congee pork", "congee chicken", "yu sheng",
    "lu rou fan", "zhajiangmian", "pork belly buns", "stinky tofu", "tteokbokki spicy", "kimbap",
    "bibimbap", "naengmyeon", "galbi beef", "samgyetang", "gamjatang", "dak galbi", "yangnyeom chicken",
    "dakgangjeong", "soondubu jjigae", "soju", "makgeolli", "baekseju", "cheongju", "bingsu red bean",
    "bingsu mango", "hotteok", "injeolmi", "chapchae", "kimchi pancake", "gimbap tuna", "gimbap beef",
    "gimbap chicken", "mandu soup", "ramyeon instant", "korean fried chicken", "dakgangjeong spicy",
    "yangnyeom chicken sweet", "honey soy chicken", "bulgogi beef", "spicy pork bulgogi"
    ]
    food_labels += [
    "churros", "tres leches cake", "flan", "arroz con leche", "empanadas beef", "empanadas chicken",
    "arepas", "pabellon criollo", "ceviche peru", "ceviche ecuador", "ceviche mexico", "tamales", 
    "taco al pastor", "taco carnitas", "taco fish", "quesadilla cheese", "quesadilla chicken",
    "enchiladas", "burrito bowl", "chilaquiles", "pozole", "menudo", "sopes", "gorditas", "molletes",
    "elote", "papas bravas", "paella seafood", "paella valenciana", "tortilla española", "gazpacho",
    "salmorejo", "empanadillas", "croquetas", "tapas mixed", "patatas alioli", "chorizo", "jamon iberico",
    "pulpo a la gallega", "fabada asturiana", "cochinillo asado", "lechazo asado", "pisto", "migas",
    "ratatouille", "quiche lorraine", "coq au vin", "bouillabaisse", "cassoulet", "salade niçoise",
    "soupe à l'oignon", "crêpes sucrées", "crêpes salées", "tarte tatin", "clafoutis", "madeleines",
    "pain au chocolat", "éclairs", "profiteroles", "mousse au chocolat", "macarons", "brioche", "fondue cheese",
    "fondue chocolate", "raclette", "schnitzel veal", "schnitzel chicken", "spätzle", "pretzel", 
    "bratwurst", "currywurst", "kartoffelsalat", "leberkäse", "goulash hungarian", "langos", "palacsinta",
    "pierogi potato", "pierogi meat", "bigos", "zurek", "kotlet schabowy", "sauerkraut", "babka cake",
    "paczki", "blintzes", "borscht beet", "pelmeni meat", "okroshka", "shashlik", "plov uzbek", 
    "manty uzbek", "lagman", "khachapuri", "khinkali", "lobiani", "churchkhela", "baklava turkish", 
    "kunefe", "lokum", "börek", "simit", "manti turkish", "kofte", "doner kebab", "adana kebab",
    "lahmacun", "pide", "menemen", "imam bayildi", "dolma", "sarma", "meze platter", 
    "hummus tahini", "baba ganoush", "tabbouleh", "fattoush", "falafel pita", "shawarma chicken", 
    "shawarma beef", "kofta kebab", "kebab platter", "mansaf", "maqluba", "fattah", "kabsa", "moujadara",
    "biryani chicken", "biryani lamb", "biryani veg", "butter chicken", "chicken tikka masala", 
    "saag paneer", "aloo gobi", "dal makhani", "chole masala", "rajma masala", "palak paneer", 
    "malai kofta", "gobi manchurian", "paneer butter masala", "korma lamb", "korma chicken", 
    "vindaloo lamb", "vindaloo chicken", "pav bhaji", "vada pav", "pani puri", "golgappa", "dahi puri",
    "sev puri", "sambar", "rasam", "idli", "dosa masala", "uttapam", "poha", "upma", "puran poli",
    "modak steamed", "bhakri", "thepla", "dhokla", "khandvi", "fafda", "ghughra", "chakli", "karanji",
    "sohan papdi", "besan ladoo", "motichoor ladoo", "tilgul", "peda milk", "barfi cashew", "rasmalai",
    "kheer rice", "phirni rice", "jalebi sugar", "gulab jamun syrup", "imarti", "balushahi"
    ]
    food_labels += [
    "apple", "banana", "orange", "grape", "strawberry", "blueberry", "raspberry", "blackberry", 
    "watermelon", "cantaloupe", "honeydew", "kiwi", "pineapple", "mango", "papaya", "peach", 
    "nectarine", "plum", "pear", "cherry", "apricot", "pomegranate", "fig", "date", "coconut", 
    "lemon", "lime", "grapefruit", "tangerine", "mandarin", "avocado", "tomato", "cucumber", 
    "lettuce", "spinach", "kale", "arugula", "romaine lettuce", "cabbage", "broccoli", "cauliflower",
    "brussels sprouts", "carrot", "celery", "bell pepper", "jalapeno", "chili pepper", "zucchini", 
    "squash", "pumpkin", "sweet potato", "potato", "onion", "garlic", "ginger", "beet", "radish",
    "turnip", "parsnip", "leek", "okra", "eggplant", "mushroom", "pea", "green beans", "snow peas",
    "edamame", "asparagus", "artichoke", "corn", "cabbage red", "collard greens", "mustard greens",
    "watercress", "bok choy", "endive", "fennel", "rhubarb", "bamboo shoots", "bean sprouts",
    "aloe vera", "sweet corn", "baby corn", "seaweed", "nori", "spinach baby", "microgreens", 
    "pumpkin seeds", "sunflower seeds", "chia seeds", "flax seeds", "hemp seeds", "walnut", "almond",
    "cashew", "pecan", "hazelnut", "macadamia nut", "brazil nut", "pine nut", "peanut", "pistachio",
    "cabbage savoy", "cabbage napa", "carrot purple", "potato red", "potato white", "potato yukon gold",
    "apple green", "apple red", "apple yellow", "pear green", "pear red", "grape red", "grape green",
    "grape black", "kiwi green", "kiwi golden", "plum red", "plum yellow", "cherry red", "cherry black",
    "strawberry large", "strawberry small", "blueberry wild", "raspberry red", "raspberry black",
    "blackberry wild", "mango ripe", "mango unripe", "pineapple ripe", "pineapple unripe",
    "cantaloupe ripe", "cantaloupe unripe", "watermelon seedless", "watermelon seeded", 
    "tangerine small", "mandarin small", "lemon yellow", "lime green", "grapefruit pink", 
    "grapefruit white", "tomato cherry", "tomato plum", "tomato heirloom", "tomato roma", 
    "bell pepper red", "bell pepper yellow", "bell pepper green", "jalapeno fresh", "chili red", 
    "chili green", "zucchini green", "zucchini yellow", "eggplant small", "eggplant large",
    "cucumber english", "cucumber pickling", "lettuce iceberg", "lettuce romaine", "lettuce red leaf",
    "lettuce green leaf", "spinach fresh", "spinach frozen", "kale curly", "kale lacinato",
    "arugula fresh", "broccoli fresh", "broccoli frozen", "cauliflower fresh", "cauliflower frozen",
    "brussels sprouts fresh", "brussels sprouts frozen", "carrot fresh", "carrot baby", "celery sticks",
    "onion yellow", "onion white", "onion red", "garlic fresh", "garlic roasted", "ginger fresh",
    "ginger powdered", "beet red", "beet golden", "radish red", "radish white", "parsnip fresh",
    "leek fresh", "okra fresh", "mushroom button", "mushroom portobello", "mushroom shiitake",
    "pea green", "green beans fresh", "green beans frozen", "snow peas fresh", "edamame frozen",
    "asparagus green", "asparagus white", "artichoke globe", "artichoke baby", "corn sweet", 
    "corn popcorn", "corn frozen", "bok choy baby", "bok choy large", "endive belgian", "fennel bulb",
    "rhubarb fresh", "bamboo shoots canned", "bean sprouts mung", "aloe vera fresh", "pumpkin fresh",
    "pumpkin canned", "sweet potato orange", "sweet potato purple", "sweet potato white", "nut mix",
    "walnut halves", "almond whole", "cashew halves", "pecan halves", "hazelnut roasted", "macadamia roasted",
    "brazil nut whole", "pine nut raw", "peanut roasted", "pistachio salted", "chia seeds raw",
    "flax seeds whole", "hemp seeds shelled", "rice white", "rice brown", "rice basmati", "rice jasmine",
    "rice wild", "rice arborio", "quinoa", "oats rolled", "oats steel cut", "barley", "millet", "buckwheat",
    "cornmeal", "wheat flour", "all purpose flour", "whole wheat flour", "rye flour", "spelt flour",
    "semolina", "pasta spaghetti", "pasta penne", "pasta fusilli", "pasta macaroni", "pasta farfalle",
    "pasta lasagna", "bread white", "bread whole wheat", "bread multigrain", "bread rye", "bagel plain",
    "bagel sesame", "bagel poppy", "croissant butter", "muffin blueberry", "muffin chocolate", 
    "pita bread", "tortilla flour", "tortilla corn", "naan bread", "chapati", "roti", "flatbread", 
    "pancake plain", "waffle plain", "oatmeal plain", "cereal corn flakes", "cereal oats", 
    "cereal granola", "cereal muesli", "cereal rice crispies", "milk whole", "milk skim", "milk almond",
    "milk soy", "milk oat", "yogurt plain", "yogurt greek", "cheese cheddar", "cheese mozzarella",
    "cheese gouda", "cheese parmesan", "cheese brie", "cheese feta", "cheese swiss", "cheese blue",
    "egg chicken", "egg duck", "egg quail", "chicken breast", "chicken thigh", "chicken drumstick",
    "chicken wings", "beef ground", "beef steak", "beef roast", "pork chop", "pork belly", 
    "pork ribs", "lamb chops", "lamb leg", "fish salmon", "fish cod", "fish tilapia", "fish tuna", 
    "shrimp raw", "shrimp cooked", "crab", "lobster", "clams", "mussels", "oysters", "squid", "octopus",
    "tofu firm", "tofu soft", "tempeh", "seitan", "beans black", "beans kidney", "beans pinto", 
    "beans garbanzo", "lentils red", "lentils green", "lentils brown", "peas split", "peas green dried",
    "peanuts raw", "peanuts roasted", "almonds raw", "cashews raw", "walnuts raw", "hazelnuts raw",
    "pumpkin seeds roasted", "sunflower seeds roasted", "chia seeds ground", "flax seeds ground",
    "sesame seeds", "coconut shredded", "coconut milk", "olive oil", "canola oil", "sunflower oil",
    "butter unsalted", "butter salted", "margarine", "honey", "syrup maple", "syrup chocolate", 
    "sugar white", "sugar brown", "sugar powdered", "salt table", "salt sea", "pepper black",
    "pepper white", "paprika", "cumin", "turmeric", "coriander", "basil dried", "oregano dried", 
    "thyme dried", "rosemary dried", "parsley fresh", "cilantro fresh", "dill fresh", "chives fresh", 
    "mint fresh", "lemon juice", "lime juice", "vinegar balsamic", "vinegar apple cider", "vinegar white"
    ]
    food_labels += [
    "apple", "banana", "orange", "grape", "strawberry", "blueberry", "raspberry",
    "blackberry", "kiwi", "pineapple", "mango", "papaya", "pear", "peach", "plum",
    "cherry", "apricot", "nectarine", "pomegranate", "watermelon", "cantaloupe",
    "honeydew", "lemon", "lime", "grapefruit", "tangerine", "clementine", "mandarin",
    "fig", "guava", "lychee", "passion fruit", "dragon fruit", "jackfruit", "durian",
    "persimmon", "starfruit", "cranberry", "currant", "elderberry", "mulberry",
    "boysenberry", "gooseberry", "avocado", "coconut", "date", "olive", "quince",
    "rhubarb", "tomato", "bell pepper", "chili pepper", "jalapeno", "habanero",
    "cayenne pepper", "poblano", "banana pepper", "carrot", "beet", "radish", "turnip",
    "parsnip", "rutabaga", "sweet potato", "potato", "yam", "onion", "red onion",
    "yellow onion", "white onion", "shallot", "scallion", "leek", "garlic", "ginger",
    "turmeric", "celery", "fennel", "bok choy", "cabbage", "savoy cabbage",
    "napa cabbage", "kale", "spinach", "arugula", "lettuce", "romaine lettuce",
    "iceberg lettuce", "endive", "radicchio", "chard", "collard greens", "mustard greens",
    "watercress", "broccoli", "broccolini", "cauliflower", "brussels sprouts",
    "asparagus", "artichoke", "okra", "eggplant", "zucchini", "squash", "pumpkin",
    "cucumber", "corn", "green beans", "snap peas", "snow peas", "pea pods", "mushroom",
    "shiitake mushroom", "portobello mushroom", "button mushroom", "oyster mushroom",
    "enoki mushroom", "truffle", "chestnut", "almond", "cashew", "walnut", "pecan",
    "hazelnut", "macadamia", "pistachio", "sunflower seeds", "pumpkin seeds", "chia seeds",
    "flax seeds", "sesame seeds", "soybean", "edamame", "lentil", "chickpea", "black bean",
    "kidney bean", "pinto bean", "navy bean", "cannellini bean", "fava bean", "mung bean",
    "aduki bean", "broad bean", "cucumber pickle", "jalapeno pickle", "beetroot", "watercress",
    "mizuna", "daikon", "kohlrabi", "celeriac", "seaweed", "nori", "wakame", "kelp",
    "spirulina", "algae", "corn salad", "tat soi", "endive", "frisee", "mushroom truffle",
    "morel mushroom", "chanterelle mushroom", "porcini mushroom", "hen-of-the-woods",
    "shiitake mushroom dried", "bok choy baby", "pak choi", "baby spinach", "baby kale",
    "microgreens", "pea shoots", "radish sprouts", "sunflower sprouts", "beet greens",
    "turnip greens", "mustard greens baby", "water spinach", "celtuce", "broccoli rabe",
    "rapini", "fiddlehead fern", "lotus root", "bamboo shoots", "cactus", "nopales",
    "okra baby", "okra regular", "bell pepper red", "bell pepper green", "bell pepper yellow",
    "tomatillo", "habanero pepper", "serrano pepper", "anaheim pepper", "poblano pepper",
    "thai chili", "cayenne chili", "ghost pepper", "scotch bonnet", "carrot baby", "carrot orange",
    "carrot purple", "carrot yellow", "beet red", "beet golden", "beet chioggia", "radish red",
    "radish white", "radish black", "turnip purple top", "turnip white", "rutabaga yellow",
    "sweet corn", "baby corn", "potato russet", "potato red", "potato white", "yam purple",
    "yam white", "onion red", "onion yellow", "onion white", "garlic fresh", "garlic black",
    "leek baby", "leek large", "ginger fresh", "ginger dried", "turmeric fresh", "turmeric dried",
    "celery stalk", "celery root", "fennel bulb", "fennel fronds", "cabbage green", "cabbage red",
    "cabbage savoy", "kale curly", "kale lacinato", "spinach baby", "spinach regular", "arugula baby",
    "lettuce butterhead", "lettuce romaine", "lettuce iceberg", "lettuce oak leaf", "endive green",
    "radicchio red", "chard rainbow", "chard green", "collard greens", "mustard greens regular",
    "watercress peppery", "broccoli head", "broccoli stem", "broccolini", "cauliflower white",
    "cauliflower purple", "cauliflower orange", "brussels sprouts green", "asparagus green",
    "asparagus white", "artichoke globe", "artichoke baby", "okra green", "okra red", "eggplant purple",
    "eggplant white", "zucchini green", "zucchini yellow", "squash summer", "squash winter",
    "pumpkin orange", "pumpkin white", "cucumber green", "cucumber yellow", "corn ear", "green beans",
    "snap peas sugar", "snow peas", "pea pods", "mushroom button", "mushroom portobello",
    "mushroom shiitake", "mushroom oyster", "mushroom enoki", "truffle black", "truffle white"
    ]
    food_labels += [
    "oreo", "chocolate chip cookie", "sugar cookie", "gingerbread cookie", "macaron", 
    "brownie", "blondie", "snickerdoodle", "shortbread", "biscuits", "graham cracker",
    "rice krispies treat", "candy cane", "lollipop", "gummy bears", "gummy worms", "gummy snakes",
    "marshmallow", "peanut brittle", "toffee", "fudge", "caramel", "caramel chews", "butterscotch",
    "candy bar", "kitkat", "reeses peanut butter cup", "snickers", "twix", "milky way", "mars bar",
    "hershey bar", "toblerone", "m&m's", "skittles", "jelly beans", "sour patch kids", "starburst",
    "sweet tarts", "jawbreakers", "chocolate truffle", "praline", "nougat", "licorice", "chocolate coin",
    "popcorn", "buttered popcorn", "caramel popcorn", "cheddar popcorn", "kettle corn", "microwave popcorn",
    "potato chips", "lays classic", "doritos nacho cheese", "doritos cool ranch", "ruffles", "pringles original",
    "pringles sour cream", "tortilla chips", "tostitos", "cheetos", "cheetos crunchy", "cheetos puffs",
    "cheese balls", "pretzels", "soft pretzel", "hard pretzel sticks", "pretzel twists", "pita chips",
    "bagel chips", "cracker", "cheese cracker", "graham cracker", "saltine cracker", "rice cracker",
    "trail mix", "granola bar", "nut bar", "protein bar", "fruit bar", "energy bar", "pop tarts",
    "danish pastry", "cinnamon roll", "croissant chocolate", "apple turnover", "danish cheese", "danish cherry",
    "muffin blueberry", "muffin chocolate chip", "muffin banana", "cupcake vanilla", "cupcake chocolate",
    "cupcake red velvet", "donut glazed", "donut chocolate", "donut powdered", "donut jelly", "cake slice",
    "slice chocolate cake", "slice vanilla cake", "slice carrot cake", "slice red velvet", "slice sponge cake",
    "cheesecake slice", "ice cream cone", "ice cream scoop vanilla", "ice cream scoop chocolate",
    "ice cream sundae", "ice cream sandwich", "popsicle", "frozen yogurt cup", "gelato", "sorbet",
    "churros", "candy corn", "peanut butter cup", "twizzlers", "licorice black", "marshmallow fluff",
    "candy coated chocolate", "sour gummy", "fruit gummy", "chocolate covered pretzel", "chocolate covered almond",
    "chocolate covered peanut", "chocolate covered raisins", "chocolate dipped fruit", "pop tart frosted",
    "rice krispies square", "cake pop", "mini cupcake", "mini donut", "wafer chocolate", "wafer vanilla",
    "pocky chocolate", "pocky strawberry", "snack mix", "chex mix", "cracker jack", "chips ahoy", "nutter butter",
    "reese's pieces", "butterfinger", "baby ruth", "milky way bite", "hershey kiss", "hershey nugget",
    "cadbury dairy milk", "ferrero rocher", "lindt truffle", "toblerone bite", "m&m peanut", "m&m crispy",
    "skittles original", "skittles sour", "starburst original", "starburst tropical", "warheads", "sour punch",
    "twix mini", "twix fun size", "snickers mini", "snickers fun size", "kitkat mini", "kitkat fun size",
    "twizzlers bite size", "nerds", "jelly belly", "gushers", "fruit by the foot", "fruit roll up",
    "candy necklace", "candy bracelet", "tootsie roll", "tootsie pop", "chocolate bunny", "peeps", "marshmallow bunny",
    "s'mores", "graham cracker square", "chocolate square", "marshmallow square", "popcorn ball", "corn chip",
    "nachos cheese", "nachos supreme", "soft pretzel bite", "cheese stick", "string cheese", "mozzarella stick",
    "jalapeno popper", "potato wedge", "sweet potato fry", "curly fry", "tater tot", "onion ring", "cheese curd",
    "chicken nugget", "chicken strip", "mini pizza", "pizza roll", "mini calzone", "mini quiche", "spring roll",
    "egg roll", "samosa", "empanada", "pita pocket", "breadstick", "garlic breadstick", "cheese bread",
    "stuffed bread", "pretzel dog", "corn dog", "bagel plain", "bagel sesame", "bagel everything", "cracker sandwich",
    "peanut butter sandwich", "jelly sandwich", "nutella sandwich", "fruit sandwich", "cheese sandwich",
    "ham sandwich", "turkey sandwich", "club sandwich", "BLT sandwich", "sub sandwich", "hoagie",
    "wrap sandwich", "taco", "mini taco", "taquito", "burrito snack", "quesadilla snack", "enchilada snack",
    "nacho chip snack", "pita chip snack", "chips and dip", "guacamole dip", "salsa dip", "hummus dip",
    "spinach dip", "artichoke dip", "cheese dip", "buffalo wings snack", "fried chicken bite", "meatball bite",
    "sausage bite", "hot dog mini", "mini burger", "slider burger", "pizza slider", "mini pie", "hand pie",
    "fruit tart", "mini tart", "candy bar bite", "chocolate bite", "candy bag", "treat bag", "snack pack",
    "trail mix pack", "granola pack", "cookie pack", "crackers pack", "chips pack", "nuts pack", "dried fruit pack",
    "fruit cup", "fruit salad", "veggie cup", "veggie sticks", "apple slices", "banana chips", "carrot sticks",
    "celery sticks", "cucumber slices", "bell pepper slices", "cherry tomatoes", "grape tomatoes", "olive snack",
    "pickles snack", "mini pretzels pack", "popcorn pack", "cheese cube snack", "cheese string snack", "cheese wedge",
    "yogurt cup", "yogurt parfait", "pudding cup", "jello cup", "gelatin snack", "fruit snack", "fruit leather",
    "fruit gummy snack", "raisins snack", "dried apricot", "dried fig", "dried banana", "dried mango",
    "dried pineapple", "dried apple", "dried cherry", "dried blueberry", "dried cranberry", "dried goji berry",
    "energy bite", "protein bite", "protein ball", "granola bite", "trail mix bite", "cereal bar", "nut bar",
    "rice cake snack", "rice cake chocolate", "rice cake peanut butter", "wafer snack", "wafer chocolate", "wafer vanilla",
    "pocky snack", "pretzel rod", "pretzel twist", "pretzel nugget", "mini muffin", "mini cake", "mini brownie",
    "mini cookie", "mini donut", "fun size candy", "bite size candy", "candy assortment", "snack assortment",
    "party mix", "french fry snack", "chips snack", "crisps", "potato chip snack", "tortilla chip snack",
    "corn chip snack", "cheese puff snack", "cheese ball snack", "cheese curl", "cheese stick snack",
    "chocolate snack", "chocolate candy", "chocolate truffle snack", "chocolate fudge bite", "chocolate bar snack",
    "caramel snack", "toffee bite", "candy corn snack", "marshmallow snack", "marshmallow treat",
    "sweet roll", "cinnamon twist", "cinnamon bun snack", "fruit pastry", "mini danish", "danish pastry snack",
    "handheld pastry", "pie snack", "mini pie snack", "poptart snack", "cake pop snack", "donut hole",
    "donut mini", "ice cream snack", "frozen yogurt snack", "gelato snack", "sorbet snack", "pudding snack",
    "yogurt snack", "cheese snack", "cheese cube", "cheese wedge", "cheese stick", "cheese slice"
    ]
    food_labels = list(dict.fromkeys(food_labels))
    
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