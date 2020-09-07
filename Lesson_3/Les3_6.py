x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 - 1 == x2 or x1 + 1 == x2 and y1 - 2 == y2 or y1 + 2 == y2 and x1 - 2 == x2 or x1 + 2 == x2 and y1 - 1 == y2 or y1 + 1 == y2:
    print("Can go")
else:
    print("Can't go")
