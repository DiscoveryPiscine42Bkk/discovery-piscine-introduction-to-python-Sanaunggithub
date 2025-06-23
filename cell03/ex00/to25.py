#!/c/Python313/python
import sys

number = int(input("Enter a number less than 25 : "))

if number > 25:
    sys.exit("Error")

i = number

while i <= 25:
    print("Inside the loop,  my variable is", i)
    i += 1
