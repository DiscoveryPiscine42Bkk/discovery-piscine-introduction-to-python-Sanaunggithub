#!/c/Python313/python
i = 0
while i < 11:
    print(f"Table de {i}: ", end="")

    j = 0

    while j < 11:
        print(i * j, end=" ")
        j += 1
    i += 1
    print()