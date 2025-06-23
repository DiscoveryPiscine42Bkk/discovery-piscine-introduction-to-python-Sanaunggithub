#!/c/Python313/python

word = input("")

for c in word:
    if c.isupper():
        print(c.lower(), end="")
    
    else:
        print(c.upper(), end="")