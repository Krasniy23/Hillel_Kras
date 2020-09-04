import random
num = int(input("Enter number: "))
numbers = random.sample(range(10), 1)
for data in numbers:
    if num <= data:
        print("You WON!")
        break
    if num >= data:
        print("You lose!")
        break
print(''.join(map(str, numbers)))
