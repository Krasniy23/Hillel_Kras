import json
from datetime import timedelta
from pprint import pprint

with open("acdc.json") as f:
    data = json.load(f)
    duration = [int(track['duration']) for track in data['album']['track']['track']]
    pprint(timedelta(seconds=sum(duration)