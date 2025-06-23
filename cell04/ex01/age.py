#!/c/Python313/python

age = int(input("please tell me your age: "))

print(f"You are currently {str(age)} years old")

count = 10

while count <= 30:
    age = age + 10
    print(f"In {count} years, you'll be {age} years old.")
    count += 10