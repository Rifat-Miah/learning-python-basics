import json 
def write_json(data, filename = "names.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent= 4)

with open("names.json") as json_file:
    data = json.load(json_file)
    temp = data["names"]
    x = {"firstname": "Jahid", "age": 15}
    y = {"firstname": "Nahid", "age": 45}
    temp.append(x)
    temp.append(y)

write_json(data)