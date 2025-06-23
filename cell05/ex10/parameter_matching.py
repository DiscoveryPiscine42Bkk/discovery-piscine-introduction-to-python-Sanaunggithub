#!/c/Python313/python

import sys

if len(sys.argv) == 1:
    print("none")

else:
    word = sys.argv[1]
    user = input("What was the parameter? ")
    
    if word == user:
        print("Good job!")

    else:
        print("Nope, sorry...")