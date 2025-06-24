#!/c/Python313/python

import sys

if len(sys.argv) == 1:
    print("none")

else:
    words = sys.argv[1:]
    
    for word in words:
        print(word.upper(), end="")