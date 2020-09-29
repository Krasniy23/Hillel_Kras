import requests
import json

#currency_USD = input('Enter convert: ')

class Currency:
    convert = requests.get('https://api.exchangerate.host/convert')
    convert_data = json.loads(convert.text)
    print(convert)

with open() as file_objects:
    