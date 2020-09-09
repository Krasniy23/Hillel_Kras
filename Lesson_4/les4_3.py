a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)