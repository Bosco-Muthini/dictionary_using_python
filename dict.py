import json
import difflib

# Load dictionary data from JSON file
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to get definition of a word
def get_definition(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        # Find similar words using difflib
        similar_words = difflib.get_close_matches(word, dictionary.keys())
        if similar_words:
            suggestion = similar_words[0]
            confirm = input(f"Did you mean '{suggestion}' instead of '{word}'? (yes/no): ").lower()
            if confirm == 'yes':
                return dictionary[suggestion]
        return "Word not found in dictionary."

# Main function
def main():
    dictionary = load_dictionary('dictionary.json')
    word = input("Enter a word: ")
    definition = get_definition(word, dictionary)
    print(definition)

if __name__ == "__main__":
    main()
