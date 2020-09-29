file_name = input('Cоздать новый файл: ')
with open(file_name, 'w') as file:
    while True:
        s = input()
        if s == '':
            break
        file.write(s + '\n')