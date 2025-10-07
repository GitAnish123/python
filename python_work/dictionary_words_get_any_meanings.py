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