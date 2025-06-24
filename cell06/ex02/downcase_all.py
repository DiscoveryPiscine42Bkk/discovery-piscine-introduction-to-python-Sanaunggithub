#!/c/Python313/python

import sys

def downcase_all(word):
    return word.lower()


if len(sys.argv) == 1:
    sys.exit('none')

words = sys.argv[1:]

for word in words:
    print(downcase_all(word))
