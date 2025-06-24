#!/c/Python313/python

import sys

if len(sys.argv) == 1:
    print("none")

else:  
    word = sys.argv[1:]
    print(word[0])