# Create two functions, one will show the even numbers from an array and another function will show the grade based on the marks. (marks should be asked from the user )
def show_even_numbers(arr):
    print("\n Even numbers are : ")
    for num in arr:
        if num % 2 == 0:
            print(num)

def show_grade(marks):
    if marks >= 90:
        print("Grade: A+")
    elif marks >= 85:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B+")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C+")
    elif marks >= 65:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D+")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Grade: F")
    
user_input_array = input("Enter a list of numbers separated by spaces: ")

# Split the string by spaces and convert each item into an integer
numbers = [int(num) for num in user_input_array.split()]

show_even_numbers(numbers)

marks = int(input("\nEnter your marks: "))
show_grade(marks)