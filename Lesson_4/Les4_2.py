number = 0
summa = 0
product = 1
macs = 0
index_of_max = -1
num_even_odd = -1
element = -1
while int(input()) != 0:
    element = int()
    number += 1
    summa += number
    product *= int(number)
    if element > macs:
        macs = element
        index_of_max = number
    number += 1
    if element % 2 == 0:
        num_even_odd += 1

print("Четные, Нечетные: ", num_even_odd)
print("Сумма чисел: ", summa)
print("Произведение: ", product)
print("Количество введенных чисел: ")
print("Порядковый номер: ", number)