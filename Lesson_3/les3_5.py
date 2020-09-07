import random
num = int(input("Enter number: "))
numbers = random.sample(range(10), 1)
for data in numbers:
    if num != data:
        print("You Lose!")
        break
    if num == data:
        print("You WON!")
        break
print(''.join(map(str, numbers)))


