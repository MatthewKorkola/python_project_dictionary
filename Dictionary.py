# This program acts as a dictionary.
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

# return the definition of a word
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    # account for proper nouns
    elif w.title() in data:
        return data[w.title()]
    # account for acronyms
    elif w.upper() in data:
        return data[w.upper()]
    # determine the similarity of the entered word
    # to a potential close match in the dictionary
    elif len(get_close_matches(w, data.keys())) > 0:
        keep_searching = input("Did you mean %s instead? Enter Y if yes, or anything else if no: " % get_close_matches(w, data.keys())[0])
        if keep_searching == "Y" or keep_searching == "y":
            return data[get_close_matches(w, data.keys())[0]]
    
    return "The word does not exist. Please double check it."

# loop for as long as the user wants to continue
while True:
    word = input("Enter a word to define: ")

    output = translate(word)

    if type(output) == list:
        for item in output:
            print("\n" + item)
    else:
        print("\n" + output)
    
    quit = input("\nEnter Q to quit, or anything else to continue: ")
    if quit == "Q" or quit == "q":
        break
