#!/c/Python313/python

origin = [2, 8, 9, 48, 8, 22, -12, 2]
print(origin)

new = [val + 2 for val in origin if val > 5]
s = set(new)
print(s)