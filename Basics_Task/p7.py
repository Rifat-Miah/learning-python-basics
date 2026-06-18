# Write a python program that takes a list of integers from the user. Do the following:
#     A. Remove duplicates
#     B. Sort the list in descending order
#     C. Filter out numbers divisible by 3
#     D. Return the modified list

numbers = input("Enter numbers separated by space: ").split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers = list(set(numbers))
print("After removing duplicates:", numbers)

numbers.sort(reverse = True)
print("Sorted list in descending order = ", numbers)

result = []

for num in numbers:
    if num %3 != 0:
        result.append(num)
print("After filtering numbers divisible by 3:", result)
print("Modified list: ", result)