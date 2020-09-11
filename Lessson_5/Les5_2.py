some_text = input("Введите какой то текст: ")
sym_some_text = len(some_text)
sym_some_text2 = len(some_text) - some_text.count(' ')
words = some_text.count(' ') + 1
print("Количество введенный символов: ", sym_some_text2)
print("Общее число слов:", words)



