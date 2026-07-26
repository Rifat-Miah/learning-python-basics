import json

#file = "names.json"
with open("names.json", "r") as json_file:
    data = json.load(json_file)
    print(data)                           # print dictonary
    print("\n", data["names"])            # print list

    name_data = (data["names"])
    for i in name_data:
       # print(i)                 # print individual list items

        name = (i["firstname"])
        age = (i["age"])
        print(f"{name} is {age} years old.")
