#!/c/Python313/python

import sys

if len(sys.argv) == 1:
    print("none")

else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    lst = [val for val in range(start, end + 1)]

    print(lst)