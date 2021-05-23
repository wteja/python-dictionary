import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))
keys = data.keys()

def translate(w):
    w = w.lower()
    if w in data:
        return "\n".join("- " + word for word in data[w])
    else:
        suggested_words = get_close_matches(w, keys)
        if len(suggested_words)  > 0:
            answer = input("Did you mean: %s instead? Enter Y if yes, or N if no. " % suggested_words[0]).upper()
            if answer == "Y":
                return data[suggested_words[0]]
            elif answer == "N":
                return "The word doesn't exists. Please double check it."
            else:
                return "We didn't understand your entry."
        else:
            return "The word doesn't exists. Please double check it."

print("Enter word to translate or put /end if you want to exit.")

while True:
    word = input("Enter word: ")
    if word != "/end":
        print(translate(word))
    else:
        break
