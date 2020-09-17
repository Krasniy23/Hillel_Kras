from math import sqrt

def length(x1, y2):
    dx = x1
    dy = y2
    s = sqrt(dx*dy)
    return s

print(map(int, input().split()))
