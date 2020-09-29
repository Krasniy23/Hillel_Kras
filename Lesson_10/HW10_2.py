slovo_polindrom = str(input("Введите что то и узнаем полинром это или нет: "))
value = slovo_polindrom[::-1]
if slovo_polindrom == value:
    print("Это полиндром, Поздравляю!")
else:
    print("А это не полиндром, Увы!")
