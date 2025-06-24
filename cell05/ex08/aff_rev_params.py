#!/c/Python313/python

import sys

if len(sys.argv) == 1:
    print("none")

else:

    if len(sys.argv) == 2:
        print('none')
    
    else:
        words = sys.argv[1:]
        reversed_words = words[::-1]
        
        for word in reversed_words:
            print(word)
       