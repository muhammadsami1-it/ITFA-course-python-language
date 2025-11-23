a = int(input("a = "))
b = int(input("b = "))
print("Enter 1 for Add 2 for Subtract 3 for Multiply")
op = int(input("operator = "))

if op == 1:
    print(a + b)
elif op == 2:
    print(a - b)
elif op == 3:
    print(a * b)
else:
    print('"Invalid Input"')