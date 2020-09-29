slovo_polindrom = str(input())
a = slovo_polindrom[::-1]
if slovo_polindrom == a:
    print("это полиндром")
else:
    print("а это не полиндром")
