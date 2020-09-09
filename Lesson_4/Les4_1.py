x = int(input("Enter the first  day kilometers: "))
y = int(input("Enter the second  day kilometers: "))
i = 1
while x < y:
    x *= 1.1
    i += 1
print("Day number: " + str(i))
