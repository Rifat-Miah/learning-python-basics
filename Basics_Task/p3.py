# Write a python program to to calculate the factorial of given number.(take input from the user)
num = int(input("Enter a number: "))

fact = 1
for i in range(1, num+1):
    fact = fact * i
print("factorial = ", fact)