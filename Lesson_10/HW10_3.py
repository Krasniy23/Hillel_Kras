def shift(some_list, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            some_list.append(some_list.pop(0))
    else:
        for i in range(steps):
            some_list.insert(0, some_list.pop())


nums = [4, 5, 6, 7, 8, 9, 0]
shift(nums, 5)
print(nums)
