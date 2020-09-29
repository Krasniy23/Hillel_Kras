file_name = input('Cоздать новый файл: ')
with open(file_name, 'w') as file_name:
    while True:
        s = input()
        if s == '':
            break
    file_name.write(s+'\n')
