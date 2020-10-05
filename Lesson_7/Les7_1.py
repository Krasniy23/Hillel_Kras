def count_word(function):
    print(function().split())
    return function


@count_word
def string():
    return input("ВВедите строку")
