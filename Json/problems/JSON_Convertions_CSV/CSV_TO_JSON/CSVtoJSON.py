import json
import csv

with open("names.csv", "r") as f:
    reader = csv.reader(f)     # create a csv reader
    next(reader)               # create csv header row ["firstname", "age"]
    data = {"names": []}       # create empty dictionary

    for row in reader:         # loop for each row 
        print(row)
        if not row:             # Skip empty rows
            continue
        data["names"].append({"firstname": row[0], "age": row[1]})  # add data in dictionary

with open("namesNew.json", "w") as f:
    json.dump(data, f, indent= 4)
    '''
    json.dump() writes a Python object to a JSON file.
    indent=4 formats the JSON with 4 spaces of indentation to make it easier to read.
    '''