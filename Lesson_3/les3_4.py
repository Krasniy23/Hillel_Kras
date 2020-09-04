num_list = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
for num in num_list:
    num_list = num / 5
    if num > 150:
        print(":(")
    print(num_list)
