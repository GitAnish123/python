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