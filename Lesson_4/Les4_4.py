number = int(input("Enter the number for number ladder: "))
for i in range(1, number + 1):
    for some_number in range(1, i + 1):
        print(some_number, sep='', end='')
    print()
