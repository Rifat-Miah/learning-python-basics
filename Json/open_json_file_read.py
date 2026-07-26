import json
from pprint import pprint

with open("students.json", "r") as f:
    data = json.load(f)
    print(data)

    pprint(data)  # pprint : formats complex data structures like deeply nested dictionaries, lists, and JSON into a clean, human-readable layout.