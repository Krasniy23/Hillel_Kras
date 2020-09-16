import datetime

date = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))
try:
    data = datetime.date(year, month, date)
    print(data)
    print("True")
except ValueError:
    print("False")
