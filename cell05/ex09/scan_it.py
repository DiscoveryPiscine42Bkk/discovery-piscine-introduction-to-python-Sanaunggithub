#!/c/Python313/python

import sys
import re

if len(sys.argv) == 1:
    print("none")

else:
    if len(sys.argv) == 2:
        print('none')
    
    else:
        pattern = sys.argv[1]
        string = sys.argv[2]

        matches = re.findall(pattern, string)

        print(len(matches))

