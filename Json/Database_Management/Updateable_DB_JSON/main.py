import json 

filename = "./data/data.json"
def Choice():
    print("R I F A T")
    print("Database Management System")
    print("(1) View Data")
    print("(2) Exit Data")
    print("(3) Exit...")

def view_data():
    with open (filename, "r") as f:
        temp = json.load(f)
    for entry in temp:
        name = entry["name"]
        begin = entry["begin"]
        end = entry["end"]
        print(f"Name is : {name}")
        print(f"Begin   : {begin}")
        print(f"End     : {end}")
        print("\n\n")

def add_data():
    with open(filename, "r") as f:
        temp = json.load(f)

    item_data = {
        "name": input("Enter name : "),
        "begin": input("Begin      : "),
        "end": input("End        : ")
    }

    temp.append(item_data)

    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)

while True:
    Choice()
    Choice = input("\n Enter Number: ")
    if Choice == "1":
        view_data()
    elif Choice == "2":
        add_data()
    elif Choice == "3":
        break
    else:
        print("You did not select a number. Please read more carefully.")
        
