import json 

filename = "./data/data.json"
def Choice():
    print("R I F A T")
    print("Database Management System")
    print("(1) View Data")
    print("(2) Add Data")
    print("(3) Delete Data")
    print("(4) Edit Data")
    print("(5) Exit...")

def view_data():
    with open (filename, "r") as f:
        temp = json.load(f)
    i = 0
    for entry in temp:
        name = entry["name"]
        begin = entry["begin"]
        end = entry["end"]

        print(f"Index Number {i}")
        print(f"Name is : {name}")
        print(f"Begin   : {begin}")
        print(f"End     : {end}")
        print("\n\n")
        i = i+1

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

def delete_data():
    view_data()
    new_data = []
    with open(filename, "r") as f:
        temp = json.load(f)
        data_length = len(temp) - 1
    print("Which index number you want to delete.")
    delete_option = input(f"Enter a number (0 - {data_length}) : ")

    i = 0
    for entry in temp:
        if i == int(delete_option):
            pass
            i = i+1

        else:
            new_data.append(entry)
            i = i+1
    with open(filename, "w") as f:
        json.dump(new_data, f, indent=4)

def edit_data():
    view_data()
    new_data = []
    with open(filename, "r") as f:
        temp = json.load(f)
        data_length = len(temp) - 1
    print(f"Which index number you want to edit?")
    edit_option = input(f"Enter a number (0 - {data_length}) : ")
    i = 0
    for entry in temp:
        if i == int(edit_option):
            name = entry["name"]
            begin = entry["begin"]
            end = entry["end"]

            print(f"Current Name is : {name}")
            name = input("Enter new name that you want : ")
            print(f"Current Begin is : {begin}")
            begin = input("Enter new Begin that you want : ")
            print(f"Current End is : {end}")
            end = input("Enter new name that you want : ")

            new_data.append({"name": name, "begin": begin, "end": end})
            i = i+1
        else:
            new_data.append(entry)
            i = i+1
    with open(filename, "w") as f:
        json.dump(new_data, f, indent=4)

while True:
    Choice()
    Choice = input("\n Enter Number: ")
    if Choice == "1":
        view_data()
    elif Choice == "2":
        add_data()
    elif Choice == "3":
        delete_data()
    elif Choice == "4":
        edit_data()
    elif Choice == "5":
        break
    else:
        print("You did not select a number. Please read more carefully.")