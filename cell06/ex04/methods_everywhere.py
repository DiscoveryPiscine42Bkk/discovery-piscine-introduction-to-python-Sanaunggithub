#!/c/Python313/python

import sys

def shrink(word):
    print(word[:8])

def enlarge(word):
    
    length = len(word)

    for _ in range(length, 8):
        word += 'Z'
    
    print(word)

words = sys.argv[1:]

for word in words:
    if len(word) > 8:
        shrink(word)
    
    elif len(word) == 8:
        print(word)

    else:
        enlarge(word)