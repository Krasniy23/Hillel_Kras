import math
a = int(input('Первая сторона: '))
b = int(input('Вторая сторна: '))
c = int(input('Третья сторона: '))
p = (a+b+c)/2
S = math.sqrt(p * (p-a) * (p-b) * (p-c))
print('Площадь: ', S)
