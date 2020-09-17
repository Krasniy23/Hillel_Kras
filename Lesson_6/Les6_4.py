import json
from pprint import pprint

with open("acdc.json", "r") as f:
    data = json.loads(f.read())
    pprint(data["name"])
