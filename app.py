import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        yn= input("Did you mean %s insted? press y for yes and press n for no: " % get_close_matches(w,data.keys())[0])
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return["please check your word"]
            
        else:
            return["input should be y or n"]
    else:
        return["Sorry! Word not found,please try again"]

word=input("Enter the word: ")
output=(translate(word))
print("=================================")
for item in output:
    print("-------------------------------")
    print(item)
    print("-------------------------------")
print("=================================")