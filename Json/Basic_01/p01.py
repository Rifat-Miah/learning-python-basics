# 1.	Convert the following dictionary into JSON format.
#Student = {“ID”: 1, ”Name”: “Rifat”, ”Age”: 23, “CGPA”: 3.50} 

import json
Student = {
    "ID": 1, 
    "Name": "Rifat",
    "Age": 23, 
    "CGPA": 3.50
} 

print(type(Student))
data = json.dumps(Student)
print(data)