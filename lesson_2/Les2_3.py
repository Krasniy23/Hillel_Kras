v = int(input("Enter your distance: "))
t = int(input("Enter your time: "))
s = v * abs(t)
print((v * t) % 100)
if v > 0 and s <= 100:
    print("aaa")
elif v < 0 and s <= 100:
    print("bbb")
