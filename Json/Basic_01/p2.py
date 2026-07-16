# 2.	Access the value of age from the given data.
# Student = {“ID”: 1, ”Name”: “Rifat”, ”Age”: 23, “CGPA”: 3.50}  
import json

'''
# Solution: 1
Student = {
    "ID": 1, 
    "Name": "Rifat",
    "Age": 23, 
    "CGPA": 3.50
} 

print(Student["Age"])
'''

Student = '''{
    "ID": 1, 
    "Name": "Rifat",
    "Age": 23, 
    "CGPA": 3.50
} '''
data = json.loads(Student)
print("Age =", data["Age"])