import requests

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Word '{word}' not found.")
        return

    data = response.json()
    print(f"\nDefinitions for '{word}':\n")
    for meaning in data[0]["meanings"]:
        part_of_speech = meaning["partOfSpeech"]
        for definition in meaning["definitions"]:
            print(f"- ({part_of_speech}) {definition['definition']}")
            if 'example' in definition:
                print(f"  e.g. {definition['example']}")
    print()

# Example usage
if __name__ == "__main__":
    word = input("Enter a word: ").strip()
    get_definition(word)

"""
Flask code

from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<title>Dictionary Lookup</title>
<h1>Enter a word to define:</h1>
<form method="get">
  <input name="word" required>
  <input type="submit" value="Search">
</form>

{% if definitions %}
  <h2>Definitions for '{{ word }}':</h2>
  <ul>
    {% for part, definition, example in definitions %}
      <li><b>({{ part }})</b> {{ definition }}{% if example %}<br><i>e.g.</i> {{ example }}{% endif %}</li>
    {% endfor %}
  </ul>
{% elif error %}
  <p style="color:red;">{{ error }}</p>
{% endif %}
'''

@app.route("/", methods=["GET"])
def home():
    word = request.args.get("word", "")
    definitions = []
    error = None

    if word:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)

        if response.status_code != 200:
            error = f"Word '{word}' not found."
        else:
            data = response.json()
            try:
                for meaning in data[0]["meanings"]:
                    part = meaning["partOfSpeech"]
                    for d in meaning["definitions"]:
                        definition = d["definition"]
                        example = d.get("example", "")
                        definitions.append((part, definition, example))
            except Exception:
                error = "Error parsing data."

    return render_template_string(TEMPLATE, word=word, definitions=definitions, error=error)

if __name__ == "__main__":
    app.run()


"""




# NEW ONE


import requests
import random
from flask import Flask, request, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your-very-secure-random-secret-key"  # Change this to a random secret key

# ---------- Diverse word list (150 words approx) ----------
WORD_LIST = [
    "gravity", "photosynthesis", "algorithm", "democracy", "ecosystem",
    "bacteria", "symbiosis", "molecule", "velocity", "protein",
    "capitalism", "chlorophyll", "neuron", "evaporation", "revolution",
    "dictionary", "literature", "philosophy", "astronomy", "chemistry",
    "football", "basketball", "marathon", "tournament", "olympics",
    "baseball", "goalkeeper", "coach", "stadium", "referee",
    "university", "lecture", "campus", "professor", "degree",
    "physics", "geometry", "calculus", "statistics", "psychology",
    "economics", "marketing", "journalism", "editorial", "conference",
    "artificial", "intelligence", "robotics", "software", "hardware",
    "internet", "website", "browser", "database", "network",
    "hurricane", "tornado", "earthquake", "volcano", "tsunami",
    "music", "guitar", "piano", "orchestra", "concert",
    "theater", "drama", "comedy", "novel", "poetry",
    "biology", "cell", "organism", "mutation", "species",
    "nutrition", "vitamin", "mineral", "enzyme", "hormone",
    "law", "contract", "jury", "verdict", "trial",
    "history", "empire", "revolution", "colony", "dynasty",
    "language", "grammar", "vocabulary", "syntax", "dialect",
    "transport", "vehicle", "engine", "railway", "airport",
    "painting", "sculpture", "gallery", "museum", "exhibition",
    "climate", "temperature", "humidity", "precipitation", "forecast",
    "psychology", "cognition", "memory", "behavior", "emotion",
    "medicine", "vaccine", "surgery", "diagnosis", "therapy",
    "architecture", "bridge", "skyscraper", "monument", "design",
    "photography", "camera", "lens", "exposure", "portrait",
    "finance", "investment", "stock", "bankruptcy", "economy",
    "sport", "athlete", "tournament", "score", "referee"
]

# ---------- HTML Templates ---------- #

HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Dictionary App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f6f8fa;
            color: #333;
            max-width: 700px;
            margin: 50px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 12px;
            background: white;
        }
        h1 {
            color: #0057b7;
        }
        input[type="text"] {
            width: 70%;
            padding: 10px;
            margin-right: 10px;
            border-radius: 6px;
            border: 1px solid #aaa;
        }
        input[type="submit"], button {
            padding: 10px 16px;
            background-color: #0057b7;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        input[type="submit"]:hover, button:hover {
            background-color: #003f8a;
        }
        ul {
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <h1>📖 Dictionary App</h1>
    <form method="get" action="/">
        <input name="word" type="text" placeholder="Enter a word" value="{{ word or '' }}" required>
        <input type="submit" value="Search">
    </form>

    {% if error %}
      <p style="color:red;">{{ error }}</p>
    {% endif %}

    {% if definitions %}
      <h2>Definitions for "{{ word }}":</h2>
      <ul>
        {% for d in definitions %}
          <li>
            <b>{{ d['part_of_speech'] }}</b>: {{ d['definition'] }}
            {% if d['example'] %}
              <br><i>e.g. {{ d['example'] }}</i>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}

    <br><br>
    <form action="/game">
        <button type="submit">🎮 Play the Game</button>
    </form>
</body>
</html>
"""

QUESTION_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Level {{ level }} - Dictionary Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f7ff;
            max-width: 600px;
            margin: 60px auto;
            padding: 30px;
            background: white;
            border-radius: 10px;
            border: 1px solid #ccc;
        }
        h1 {
            color: #0057b7;
        }
        p {
            font-size: 18px;
        }
        input[type="text"] {
            width: 90%;
            padding: 12px;
            margin-top: 10px;
            border-radius: 6px;
            border: 1px solid #aaa;
            font-size: 16px;
        }
        input[type="submit"] {
            padding: 12px 20px;
            margin-top: 20px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
        }
        input[type="submit"]:hover {
            background-color: #1e7e34;
        }
    </style>
</head>
<body>
    <h1>Level {{ level }}</h1>
    <p><b>Question {{ question_number }} of 5</b></p>
    <p><b>Definition:</b> {{ definition }}</p>
    <form method="post">
        <input type="text" name="answer" placeholder="Enter the word" required autofocus autocomplete="off">
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

GAME_OVER_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Game Over</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #fff0f0;
            text-align: center;
            padding: 80px;
        }
        h1 {
            font-size: 48px;
            color: #cc0000;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            background-color: #0057b7;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
        }
        a:hover {
            background-color: #003f8a;
        }
    </style>
</head>
<body>
    <h1>❌ Game Over!</h1>
    <p>You answered incorrectly. Try again!</p>
    <a href="/">🔁 Go back to home</a>
</body>
</html>
"""

WIN_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>You Are the Master!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0fff4;
            text-align: center;
            padding: 80px;
        }
        h1 {
            font-size: 48px;
            color: #28a745;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            background-color: #0057b7;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
        }
        a:hover {
            background-color: #003f8a;
        }
    </style>
</head>
<body>
    <h1>🏆 YOU ARE THE MASTER!</h1>
    <p>Congratulations! You completed all 5 levels!</p>
    <a href="/">🏠 Back to home</a>
</body>
</html>
"""

# ---------- Helper function to get a definition ---------- #
def get_definition_for_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    # Try to find a sufficiently detailed definition
    for meaning in data[0].get("meanings", []):
        for d in meaning.get("definitions", []):
            if len(d.get("definition", "").split()) > 3:
                return d.get("definition")
    return None


# ---------- Flask Routes ---------- #

@app.route("/", methods=["GET"])
def home():
    word = request.args.get("word", "").strip()
    error = None
    definitions = []

    if word:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        if response.status_code != 200:
            error = f"Sorry, the word '{word}' was not found."
        else:
            data = response.json()
            for meaning in data[0].get("meanings", []):
                part_of_speech = meaning.get("partOfSpeech", "")
                for definition in meaning.get("definitions", []):
                    definitions.append({
                        "part_of_speech": part_of_speech,
                        "definition": definition.get("definition", ""),
                        "example": definition.get("example", "")
                    })

    return render_template_string(HOME_TEMPLATE, word=word, definitions=definitions, error=error)


@app.route("/game")
def start_game():
    session["level"] = 1
    session["question"] = 0
    session["score"] = 0

    # Select 5 unique words for the first level (no repeats within a level)
    session["questions"] = []
    level_words = random.sample(WORD_LIST, 5)
    # For each word, get the definition and only keep if found
    questions = []
    for w in level_words:
        definition = get_definition_for_word(w)
        if definition:
            questions.append({"word": w, "definition": definition})
    # If less than 5 valid questions, try to add more
    while len(questions) < 5:
        w = random.choice(WORD_LIST)
        if w not in [q["word"] for q in questions]:
            definition = get_definition_for_word(w)
            if definition:
                questions.append({"word": w, "definition": definition})
    session["questions"] = questions
    return redirect(url_for("play_level", level=1))


@app.route("/level/<int:level>", methods=["GET", "POST"])
def play_level(level):
    if "level" not in session or level != session["level"]:
        return redirect(url_for("home"))

    question_number = session.get("question", 0)

    if request.method == "POST":
        correct_word = session["questions"][question_number - 1]["word"].lower()
        user_answer = request.form["answer"].strip().lower()
        if user_answer != correct_word:
            return redirect(url_for("game_over"))

    if question_number == 5:
        session["level"] += 1
        if session["level"] > 5:
            return redirect(url_for("win"))

        # Prepare next level's 5 unique questions (no repeats within the level)
        level_words = random.sample(WORD_LIST, 5)
        questions = []
        for w in level_words:
            definition = get_definition_for_word(w)
            if definition:
                questions.append({"word": w, "definition": definition})
        while len(questions) < 5:
            w = random.choice(WORD_LIST)
            if w not in [q["word"] for q in questions]:
                definition = get_definition_for_word(w)
                if definition:
                    questions.append({"word": w, "definition": definition})
        session["questions"] = questions
        session["question"] = 0
        return redirect(url_for("play_level", level=session["level"]))

    # Show next question
    word = session["questions"][question_number]["word"]
    definition = session["questions"][question_number]["definition"]
    session["question"] = question_number + 1

    return render_template_string(
        QUESTION_TEMPLATE,
        level=level,
        question_number=question_number + 1,
        definition=definition
    )


@app.route("/game_over")
def game_over():
    return render_template_string(GAME_OVER_TEMPLATE)


@app.route("/win")
def win():
    return render_template_string(WIN_TEMPLATE)







# NEW ONE!!


import requests
import random
from flask import Flask, request, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your-very-secure-random-secret-key"  # Change this to a random secret key

# ---------- Diverse word list (150 words approx) ----------
WORD_LIST = [
    "gravity", "photosynthesis", "algorithm", "democracy", "ecosystem",
    "bacteria", "symbiosis", "molecule", "velocity", "protein",
    "capitalism", "chlorophyll", "neuron", "evaporation", "revolution",
    "dictionary", "literature", "philosophy", "astronomy", "chemistry",
    "football", "basketball", "marathon", "tournament", "olympics",
    "baseball", "goalkeeper", "coach", "stadium", "referee",
    "university", "lecture", "campus", "professor", "degree",
    "physics", "geometry", "calculus", "statistics", "psychology",
    "economics", "marketing", "journalism", "editorial", "conference",
    "artificial", "intelligence", "robotics", "software", "hardware",
    "internet", "website", "browser", "database", "network",
    "hurricane", "tornado", "earthquake", "volcano", "tsunami",
    "music", "guitar", "piano", "orchestra", "concert",
    "theater", "drama", "comedy", "novel", "poetry",
    "biology", "cell", "organism", "mutation", "species",
    "nutrition", "vitamin", "mineral", "enzyme", "hormone",
    "law", "contract", "jury", "verdict", "trial",
    "history", "empire", "revolution", "colony", "dynasty",
    "language", "grammar", "vocabulary", "syntax", "dialect",
    "transport", "vehicle", "engine", "railway", "airport",
    "painting", "sculpture", "gallery", "museum", "exhibition",
    "climate", "temperature", "humidity", "precipitation", "forecast",
    "psychology", "cognition", "memory", "behavior", "emotion",
    "medicine", "vaccine", "surgery", "diagnosis", "therapy",
    "architecture", "bridge", "skyscraper", "monument", "design",
    "photography", "camera", "lens", "exposure", "portrait",
    "finance", "investment", "stock", "bankruptcy", "economy",
    "sport", "athlete", "tournament", "score", "referee"
]

# ---------- HTML Templates ---------- #

HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Dictionary App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f6f8fa;
            color: #333;
            max-width: 700px;
            margin: 50px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 12px;
            background: white;
        }
        h1 {
            color: #0057b7;
        }
        input[type="text"] {
            width: 70%;
            padding: 10px;
            margin-right: 10px;
            border-radius: 6px;
            border: 1px solid #aaa;
        }
        input[type="submit"], button {
            padding: 10px 16px;
            background-color: #0057b7;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        input[type="submit"]:hover, button:hover {
            background-color: #003f8a;
        }
        ul {
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <h1>📖 Dictionary App</h1>
    <form method="get" action="/">
        <input name="word" type="text" placeholder="Enter a word" value="{{ word or '' }}" required>
        <input type="submit" value="Search">
    </form>

    {% if error %}
      <p style="color:red;">{{ error }}</p>
    {% endif %}

    {% if definitions %}
      <h2>Definitions for "{{ word }}":</h2>
      <ul>
        {% for d in definitions %}
          <li>
            <b>{{ d['part_of_speech'] }}</b>: {{ d['definition'] }}
            {% if d['example'] %}
              <br><i>e.g. {{ d['example'] }}</i>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}

    <br><br>
    <form action="/game">
        <button type="submit">🎮 Play the Game</button>
    </form>
</body>
</html>
"""

QUESTION_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Level {{ level }} - Dictionary Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f7ff;
            max-width: 600px;
            margin: 60px auto;
            padding: 30px;
            background: white;
            border-radius: 10px;
            border: 1px solid #ccc;
        }
        h1 {
            color: #0057b7;
        }
        p {
            font-size: 18px;
        }
        form {
            margin-top: 20px;
        }
        button {
            display: block;
            width: 100%;
            margin: 10px 0;
            padding: 12px;
            font-size: 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Level {{ level }}</h1>
    <p><b>Question {{ question_number }} of 5</b></p>
    <p><b>Definition:</b> {{ definition }}</p>
    <form method="post">
        {% for option in options %}
            <button type="submit" name="answer" value="{{ option }}">{{ option }}</button>
        {% endfor %}
    </form>
</body>
</html>
"""

GAME_OVER_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Game Over</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #fff0f0;
            text-align: center;
            padding: 80px;
        }
        h1 {
            font-size: 48px;
            color: #cc0000;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            background-color: #0057b7;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
        }
        a:hover {
            background-color: #003f8a;
        }
    </style>
</head>
<body>
    <h1>❌ Game Over!</h1>
    <p>You answered incorrectly. Try again!</p>
    <a href="/">🔁 Go back to home</a>
</body>
</html>
"""

WIN_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>You Are the Master!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0fff4;
            text-align: center;
            padding: 80px;
        }
        h1 {
            font-size: 48px;
            color: #28a745;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            background-color: #0057b7;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
        }
        a:hover {
            background-color: #003f8a;
        }
    </style>
</head>
<body>
    <h1>🏆 YOU ARE THE MASTER!</h1>
    <p>Congratulations! You completed all 5 levels!</p>
    <a href="/">🏠 Back to home</a>
</body>
</html>
"""

# ---------- Helper function to get a definition ---------- #
def get_definition_for_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    # Try to find a sufficiently detailed definition
    for meaning in data[0].get("meanings", []):
        for d in meaning.get("definitions", []):
            if len(d.get("definition", "").split()) > 3:
                return d.get("definition")
    return None


# ---------- Flask Routes ---------- #

@app.route("/", methods=["GET"])
def home():
    word = request.args.get("word", "").strip()
    error = None
    definitions = []

    if word:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        if response.status_code != 200:
            error = f"Sorry, the word '{word}' was not found."
        else:
            data = response.json()
            for meaning in data[0].get("meanings", []):
                part_of_speech = meaning.get("partOfSpeech", "")
                for definition in meaning.get("definitions", []):
                    definitions.append({
                        "part_of_speech": part_of_speech,
                        "definition": definition.get("definition", ""),
                        "example": definition.get("example", "")
                    })

    return render_template_string(HOME_TEMPLATE, word=word, definitions=definitions, error=error)


@app.route("/game")
def start_game():
    session["level"] = 1
    session["question"] = 0
    session["score"] = 0

    # Select 5 unique words for the first level (no repeats within a level)
    session["questions"] = []
    level_words = random.sample(WORD_LIST, 5)
    # For each word, get the definition and only keep if found
    questions = []
    for w in level_words:
        definition = get_definition_for_word(w)
        if definition:
            questions.append({"word": w, "definition": definition})
    # If less than 5 valid questions, try to add more
    while len(questions) < 5:
        w = random.choice(WORD_LIST)
        if w not in [q["word"] for q in questions]:
            definition = get_definition_for_word(w)
            if definition:
                questions.append({"word": w, "definition": definition})
    session["questions"] = questions
    return redirect(url_for("play_level", level=1))


@app.route("/level/<int:level>", methods=["GET", "POST"])
def play_level(level):
    if "level" not in session or level != session["level"]:
        return redirect(url_for("home"))

    question_number = session.get("question", 0)
    questions = session.get("questions", [])

    if request.method == "POST":
        correct_word = questions[question_number - 1]["word"].lower()
        user_answer = request.form["answer"].strip().lower()
        if user_answer != correct_word:
            return redirect(url_for("game_over"))

    if question_number == 5:
        session["level"] += 1
        if session["level"] > 5:
            return redirect(url_for("win"))

        # New level: get 5 valid questions
        level_words = random.sample(WORD_LIST, 5)
        new_questions = []
        for w in level_words:
            definition = get_definition_for_word(w)
            if definition:
                new_questions.append({"word": w, "definition": definition})
        while len(new_questions) < 5:
            w = random.choice(WORD_LIST)
            if w not in [q["word"] for q in new_questions]:
                definition = get_definition_for_word(w)
                if definition:
                    new_questions.append({"word": w, "definition": definition})
        session["questions"] = new_questions
        session["question"] = 0
        return redirect(url_for("play_level", level=session["level"]))

    # Show next question
    question = questions[question_number]
    correct_word = question["word"]
    definition = question["definition"]

    # Generate 3 random incorrect words (not the correct one)
    incorrect_options = random.sample([w for w in WORD_LIST if w != correct_word], 3)
    options = incorrect_options + [correct_word]
    random.shuffle(options)

    session["question"] = question_number + 1

    return render_template_string(
        QUESTION_TEMPLATE,
        level=level,
        question_number=question_number + 1,
        definition=definition,
        options=options
    )


@app.route("/game_over")
def game_over():
    return render_template_string(GAME_OVER_TEMPLATE)


@app.route("/win")
def win():
    return render_template_string(WIN_TEMPLATE)







# NEW ONE!!!!!


import requests
import random
from flask import Flask, request, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your-very-secure-random-secret-key"  # Change this to a random secret key

# ---------- Diverse word list (150 words approx) ----------
WORD_LIST = [
    "gravity", "photosynthesis", "algorithm", "democracy", "ecosystem",
    "bacteria", "symbiosis", "molecule", "velocity", "protein",
    "capitalism", "chlorophyll", "neuron", "evaporation", "revolution",
    "dictionary", "literature", "philosophy", "astronomy", "chemistry",
    "football", "basketball", "marathon", "tournament", "olympics",
    "baseball", "goalkeeper", "coach", "stadium", "referee",
    "university", "lecture", "campus", "professor", "degree",
    "physics", "geometry", "calculus", "statistics", "psychology",
    "economics", "marketing", "journalism", "editorial", "conference",
    "artificial", "intelligence", "robotics", "software", "hardware",
    "internet", "website", "browser", "database", "network",
    "hurricane", "tornado", "earthquake", "volcano", "tsunami",
    "music", "guitar", "piano", "orchestra", "concert",
    "theater", "drama", "comedy", "novel", "poetry",
    "biology", "cell", "organism", "mutation", "species",
    "nutrition", "vitamin", "mineral", "enzyme", "hormone",
    "law", "contract", "jury", "verdict", "trial",
    "history", "empire", "revolution", "colony", "dynasty",
    "language", "grammar", "vocabulary", "syntax", "dialect",
    "transport", "vehicle", "engine", "railway", "airport",
    "painting", "sculpture", "gallery", "museum", "exhibition",
    "climate", "temperature", "humidity", "precipitation", "forecast",
    "psychology", "cognition", "memory", "behavior", "emotion",
    "medicine", "vaccine", "surgery", "diagnosis", "therapy",
    "architecture", "bridge", "skyscraper", "monument", "design",
    "photography", "camera", "lens", "exposure", "portrait",
    "finance", "investment", "stock", "bankruptcy", "economy",
    "sport", "athlete", "tournament", "score", "referee"
]

# ---------- HTML Templates ---------- #

HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Dictionary App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f6f8fa;
            color: #333;
            max-width: 700px;
            margin: 50px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 12px;
            background: white;
        }
        h1 {
            color: #0057b7;
        }
        input[type="text"] {
            width: 70%;
            padding: 10px;
            margin-right: 10px;
            border-radius: 6px;
            border: 1px solid #aaa;
        }
        input[type="submit"], button {
            padding: 10px 16px;
            background-color: #0057b7;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        input[type="submit"]:hover, button:hover {
            background-color: #003f8a;
        }
        ul {
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <h1>📖 Dictionary App</h1>
    <form method="get" action="/">
        <input name="word" type="text" placeholder="Enter a word" value="{{ word or '' }}" required>
        <input type="submit" value="Search">
    </form>

    {% if error %}
      <p style="color:red;">{{ error }}</p>
    {% endif %}

    {% if definitions %}
      <h2>Definitions for "{{ word }}":</h2>
      <ul>
        {% for d in definitions %}
          <li>
            <b>{{ d['part_of_speech'] }}</b>: {{ d['definition'] }}
            {% if d['example'] %}
              <br><i>e.g. {{ d['example'] }}</i>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    {% endif %}

    <br><br>
    <form action="/instructions">
        <button type="submit">🎮 Play the Game</button>
    </form>
</body>
</html>
"""

INSTRUCTIONS_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Game Instructions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f6f8fa;
            max-width: 700px;
            margin: 50px auto;
            padding: 30px;
            border: 1px solid #ccc;
            border-radius: 12px;
            background: white;
            color: #333;
        }
        h1 {
            color: #0057b7;
        }
        p {
            font-size: 18px;
            line-height: 1.5;
        }
        button {
            padding: 12px 20px;
            background-color: #0057b7;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #003f8a;
        }
    </style>
</head>
<body>
    <h1>🎮 Game Instructions</h1>
    <p>Welcome to the Dictionary Game! You will face 5 levels. Each level has 5 questions.</p>
    <p>For each question, you will see a definition and must select the correct word.</p>
    <p>If you answer all 5 questions in a level correctly, you move to the next level.</p>
    <p>If you get any question wrong, the game is over and you can try again.</p>
    <p>Complete all 5 levels to win and get a certificate of mastery!</p>
    <form action="{{ url_for('start_game') }}">
        <button type="submit">Start Level 1</button>
    </form>
</body>
</html>
"""

NAME_INPUT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Enter Your Name</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f6f8fa;
            max-width: 700px;
            margin: 50px auto;
            padding: 30px;
            border: 1px solid #ccc;
            border-radius: 12px;
            background: white;
            color: #333;
            text-align: center;
        }
        h1 {
            color: #0057b7;
        }
        input[type="text"] {
            padding: 12px;
            width: 60%;
            font-size: 18px;
            border-radius: 6px;
            border: 1px solid #aaa;
            margin-top: 20px;
        }
        input[type="submit"] {
            margin-top: 20px;
            padding: 12px 24px;
            font-size: 18px;
            background-color: #0057b7;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #003f8a;
        }
    </style>
</head>
<body>
    <h1>🏆 You Completed All Levels!</h1>
    <p>Please enter your name to get your certificate:</p>
    <form method="post" action="{{ url_for('enter_name') }}">
        <input type="text" name="player_name" placeholder="Your name" required autofocus>
        <br>
        <input type="submit" value="Get Certificate">
    </form>
</body>
</html>
"""

CERTIFICATE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Certificate of Mastery</title>
    <style>
        body {
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, #d4e6f1, #a9cce3);
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #2c3e50;
        }
        .certificate {
            background: white;
            padding: 50px 70px;
            border: 8px solid #2980b9;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 0 30px rgba(0,0,0,0.15);
        }
        h1 {
            font-size: 50px;
            margin-bottom: 10px;
            color: #2980b9;
        }
        h2 {
            font-size: 36px;
            margin-top: 0;
        }
        p {
            font-size: 22px;
            margin: 30px 0;
        }
        .footer {
            margin-top: 40px;
            font-style: italic;
            font-size: 18px;
            color: #555;
        }
        a {
            display: inline-block;
            margin-top: 30px;
            padding: 12px 24px;
            background-color: #0057b7;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-size: 18px;
        }
        a:hover {
            background-color: #003f8a;
        }
    </style>
</head>
<body>
    <div class="certificate">
        <h1>Certificate of Mastery</h1>
        <p>This certifies that</p>
        <h2>{{ player_name }}</h2>
        <p>has successfully completed the Dictionary Game<br>by mastering all 5 levels!</p>
        <div class="footer">Keep learning and expanding your vocabulary!</div>
        <a href="{{ url_for('home') }}">🏠 Back to Home</a>
    </div>
</body>
</html>
"""

QUESTION_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Level {{ level }} - Dictionary Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f7ff;
            max-width: 600px;
            margin: 60px auto;
            padding: 30px;
            background: white;
            border-radius: 10px;
            border: 1px solid #ccc;
        }
        h1 {
            color: #0057b7;
        }
        p {
            font-size: 18px;
        }
        form {
            margin-top: 20px;
        }
        button {
            display: block;
            width: 100%;
            margin: 10px 0;
            padding: 12px;
            font-size: 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Level {{ level }}</h1>
    <p><b>Question {{ question_number }} of 5</b></p>
    <p><b>Definition:</b> {{ definition }}</p>
    <form method="post">
        {% for option in options %}
            <button type="submit" name="answer" value="{{ option }}">{{ option }}</button>
        {% endfor %}
    </form>
</body>
</html>
"""

GAME_OVER_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Game Over</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #fff0f0;
            text-align: center;
            padding: 80px;
        }
        h1 {
            font-size: 48px;
            color: #cc0000;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            background-color: #0057b7;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
        }
        a:hover {
            background-color: #003f8a;
        }
    </style>
</head>
<body>
    <h1>❌ Game Over!</h1>
    <p>You answered incorrectly. Try again!</p>
    <a href="/">🔁 Go back to home</a>
</body>
</html>
"""

WIN_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>You Are the Master!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0fff4;
            text-align: center;
            padding: 80px;
        }
        h1 {
            font-size: 48px;
            color: #28a745;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            background-color: #0057b7;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
        }
        a:hover {
            background-color: #003f8a;
        }
    </style>
</head>
<body>
    <h1>🏆 YOU ARE THE MASTER!</h1>
    <p>Congratulations! You completed all 5 levels!</p>
    <a href="/">🏠 Back to home</a>
</body>
</html>
"""

# ---------- Helper function to get a definition ---------- #
def get_definition_for_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    # Try to find a sufficiently detailed definition
    for meaning in data[0].get("meanings", []):
        for d in meaning.get("definitions", []):
            if len(d.get("definition", "").split()) > 3:
                return d.get("definition")
    return None


# ---------- Flask Routes ---------- #

@app.route("/", methods=["GET"])
def home():
    word = request.args.get("word", "").strip()
    error = None
    definitions = []

    if word:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        if response.status_code != 200:
            error = f"Sorry, the word '{word}' was not found."
        else:
            data = response.json()
            for meaning in data[0].get("meanings", []):
                part_of_speech = meaning.get("partOfSpeech", "")
                for definition in meaning.get("definitions", []):
                    definitions.append({
                        "part_of_speech": part_of_speech,
                        "definition": definition.get("definition", ""),
                        "example": definition.get("example", "")
                    })

    return render_template_string(HOME_TEMPLATE, word=word, definitions=definitions, error=error)

@app.route("/instructions")
def instructions():
    return render_template_string(INSTRUCTIONS_TEMPLATE, url_for=url_for)

@app.route("/enter_name", methods=["GET", "POST"])
def enter_name():
    if request.method == "POST":
        player_name = request.form.get("player_name", "").strip()
        if not player_name:
            # Just reload if empty
            return render_template_string(NAME_INPUT_TEMPLATE)
        return render_template_string(CERTIFICATE_TEMPLATE, player_name=player_name)
    else:
        return render_template_string(NAME_INPUT_TEMPLATE)

@app.route("/game")
def start_game():
    # Initialize the game session variables
    session["level"] = 1
    session["question"] = 0

    # Prepare 5 questions for level 1
    new_questions = []
    level_words = random.sample(WORD_LIST, 5)
    for w in level_words:
        definition = get_definition_for_word(w)
        if definition:
            new_questions.append({"word": w, "definition": definition})
    # Make sure to fill up to 5 questions
    while len(new_questions) < 5:
        w = random.choice(WORD_LIST)
        if w not in [q["word"] for q in new_questions]:
            definition = get_definition_for_word(w)
            if definition:
                new_questions.append({"word": w, "definition": definition})
    session["questions"] = new_questions

    # Redirect to the first question of level 1
    return redirect(url_for("play_level", level=1))


@app.route("/level/<int:level>", methods=["GET", "POST"])
def play_level(level):
    if "level" not in session or level != session["level"]:
        return redirect(url_for("home"))

    question_number = session.get("question", 0)
    questions = session.get("questions", [])

    if request.method == "POST":
        correct_word = questions[question_number - 1]["word"].lower()
        user_answer = request.form["answer"].strip().lower()
        if user_answer != correct_word:
            return redirect(url_for("game_over"))

    if question_number == 5:
        session["level"] += 1
        if session["level"] > 5:
            return redirect(url_for("enter_name"))

        # New level: get 5 valid questions
        level_words = random.sample(WORD_LIST, 5)
        new_questions = []
        for w in level_words:
            definition = get_definition_for_word(w)
            if definition:
                new_questions.append({"word": w, "definition": definition})
        while len(new_questions) < 5:
            w = random.choice(WORD_LIST)
            if w not in [q["word"] for q in new_questions]:
                definition = get_definition_for_word(w)
                if definition:
                    new_questions.append({"word": w, "definition": definition})
        session["questions"] = new_questions
        session["question"] = 0
        return redirect(url_for("play_level", level=session["level"]))

    # Show next question
    question = questions[question_number]
    correct_word = question["word"]
    definition = question["definition"]

    # Generate 3 random incorrect words (not the correct one)
    incorrect_options = random.sample([w for w in WORD_LIST if w != correct_word], 3)
    options = incorrect_options + [correct_word]
    random.shuffle(options)

    session["question"] = question_number + 1

    return render_template_string(
        QUESTION_TEMPLATE,
        level=level,
        question_number=question_number + 1,
        definition=definition,
        options=options
    )


@app.route("/game_over")
def game_over():
    return render_template_string(GAME_OVER_TEMPLATE)


@app.route("/win")
def win():
    return render_template_string(WIN_TEMPLATE)