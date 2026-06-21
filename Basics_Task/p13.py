# Define a dictionary to store the details of persons. Also print some data from the dictionary. [Hint: You may require nesting dictionary, lists, string inside the dictionary.]


person = {}
person["name"] = input("Enter name: ")
person["age"] = int(input("Enter age: "))
person["city"] = input("Enter your city: ")

skills = input("Enter skills separated by spaces: ").split()
person["skills"] = skills

print("\nPerson Dictionary: ")
print(person)

print("\nPerson Details ")
print("Name  : ", person["name"])
print("Age   : ", person["age"])
print("City  : ", person["city"])
print("Skills: ", person["skills"])

if len(person["skills"]) > 0:
    print("First Skills: ", person["skills"][0])

