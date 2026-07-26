# how to create a json file and pass data
import json

file = "names.json"

def write_json(data, filename = "new_names_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

with open (file, "r") as json_file:
    data = json.load(json_file)
    write_json(data)

'''
data = ["Rohan", "Shakib", "Zisan"]
write_json(data)                     # this new data also passing possible 
'''