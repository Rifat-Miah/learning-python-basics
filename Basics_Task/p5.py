# Write a python program to determine  if a given year is leap year or not. (Take input from the user)

year =  int(input("Enter the year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year.")
else:
    print("Not a leap year.")