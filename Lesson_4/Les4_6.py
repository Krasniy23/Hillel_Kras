number = [int(i) for i in input().split( )]
counter = 0
for i in range(1, len(number) - 1):
    if number[i - 1] < number[i] > number[i + 1]:
        counter += 1
print(counter)