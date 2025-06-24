#!/c/Python313/python

import sys

if len(sys.argv) == 1:
    print("none")

words = sys.argv[1:]

for word in words:
    if word.endswith('ism'):
        continue

    else:
        print(word + "ism")