# Write a python program to find the larget element in a given list of integers. (Take input from the user)

n = int(input("How may numbers you want to enter: "))

numbers = []
for i in range(n):
    num = int(input("Enter number = "))
    numbers.append(num)
print("List : ", numbers)

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("The Largest number is: ", largest)
