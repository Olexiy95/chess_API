import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

r = requests.get(" https://api.chess.com/pub/player/Olexiy95")

rr = r.json()

jprint(rr)

