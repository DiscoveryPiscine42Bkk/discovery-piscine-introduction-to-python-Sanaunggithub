#!/c/Python313/python

import sys

if not 'z' in sys.argv[1]:
    print("none")

else:
    count = 0
    for item in sys.argv[1]:
        if item == 'z':
            count += 1
    
    for _ in range(count):
        print('z', end="")