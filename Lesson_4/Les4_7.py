first_list = (len(set(input().split())))
second_list = set(input().split())
for i in first_list:
    if i in first_list:
        continue
    for j in second_list:
        if i == j:
            i.append(i)
            break
print(i)