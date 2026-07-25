import json

data = {
    "city": "Dhaka",
    "temp": 32
}

json_string = json.dumps(data)             # dict to json string
parsed = json.loads(json_string)           # json string to dict

print(parsed["city"])

#print(json_string["city"])     # error