# Define a method to add two lists and return another list
# Example: User Input:[3,4,5,1] and [6,7,2,8] , Output: [9, 11, 7, 9]

def add_list(list1, list2):
    result = []
    
    for i in range(len(list1)):
        result.append(list1[i]+list2[i])
    return result

list1 = list(map(int, input("Enter first list elements separated by space  = ").split()))
list2 = list(map(int, input("Enter second list elements seperated by space = ").split()))

print("First List   = ", list1)
print("Second List  = ", list2)

if len(list1) != len(list2):
    print("Error: Both lists must have same number of elements.")
else:
    output = add_list(list1,list2)
    print("New list after addition = ", output)