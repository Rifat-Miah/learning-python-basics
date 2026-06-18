# Write a python program to print the multiplication table of a given number.(Take input from the user)
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number ,"*", i, "=", number*i)