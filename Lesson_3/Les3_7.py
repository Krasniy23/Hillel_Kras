n = int(input("Enter number for factorials count: "))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)
