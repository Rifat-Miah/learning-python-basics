import json
import csv

with open("names.json", "r") as f:
    data = json.load(f)                     # reads the file and converts it into a Python dictionary.
    names = data["names"]

with open("names.csv", "w") as f:
    fieldnames = names[0].keys()             # names[0] means the first dictionary. and .keys() returns all dictionary keys.

    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()                     # create a CSV writer that writes dictionaries

    for name in names:                       # Loop Through Each Person
        writer.writerow(name)                # Write Each Dictionary as One Row