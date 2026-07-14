import json
from pprint import pprint

with open("students.json", "r") as f:
    data = json.load(f)
    print(data)

    pprint(data)
