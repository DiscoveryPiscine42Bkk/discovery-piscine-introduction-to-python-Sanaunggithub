#!/c/Python313/python

import sys

parameter = len(sys.argv)

if parameter == 1:
    print("none")

else:
    print("parameters: ", parameter - 1)
    
    for item in sys.argv[1:]:
        print(f"{item}: {len(item)}")