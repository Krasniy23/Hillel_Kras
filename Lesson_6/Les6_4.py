import json

with open("acdc.json", "r", encoding='utf-8') as f:
    data = json.loads(f.read())
    print(data)
