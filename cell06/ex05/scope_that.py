#!/c/Python313/python

def add_one(n):
    n += 1
    print("Inside the function", n)

value = 1
print("Before the function", value)

add_one(value)

print("After the function", value)
