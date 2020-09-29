slovo_palindrom = str(input("Введите что то и узнаем полинром это или нет: "))
value = slovo_palindrom[::-1]
if slovo_palindrom == value:
    print("Это палиндром, Поздравляю!")
else:
    print("А это не палиндром, Увы!")
