#!/c/Python313/python

def greetings(word = "noble strangers"):
    if isinstance(word, str):
        print("Hello,", word)
    
    else:
        print("Error! It was not a name.")

greetings("Alexandra")
greetings("Wil")
greetings()
greetings(42)