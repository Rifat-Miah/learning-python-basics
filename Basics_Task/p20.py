# Write a method to print name and last name from full name.
# Example: Input: Al Noman Joy , Output: First Name: Al , Last Name: Joy

def print_name(full_name):
    parts = full_name.split()

    if len(parts) < 2:
        print("Please enter at least a first name and last name.")
        return
    
    print("First Name: ", parts[0])
    print("Last Name: ", parts[-1])

full_name = input("Enter full name: ")
print_name(full_name)