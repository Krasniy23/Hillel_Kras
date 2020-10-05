dict1 = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
dict2 = {key: value for key, value in dict1.items() if value is not None}
print(dict2)
