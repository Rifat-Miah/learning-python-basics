# Create a dictionary where key should be name and value should be age: show the name of the dictionary to the user and ask them to choose a name to show his or her age.

people = {
    "Rifat": 21,
    "Rana": 24,
    "Rony": 34,
    "Rohan:": 50,
}

print("Available name are: ")

for name in people:
    print(name)

chosen_name = input("Enter a name: ").title()     # .title() capitalizes the first letter

if chosen_name in people:
    print(chosen_name, "age is ", people[chosen_name])
else:
    print("Name not found.")
