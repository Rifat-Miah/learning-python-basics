# Demonstrate some string operations. Also show uses of some string methods.

txt = input("Enter a string: ")
print("Original String: ", txt)

print("Uppercase: ", txt.upper())
print("Lower: ", txt.lower())
print("Title: ", txt.title())

print("Length of string: ", len(txt))

print("Starts with 'A' : ", txt.startswith("A"))
print("Replace 'a' with '@' : ", txt.replace("a", "@"))

print("Count of 'a': ", txt.count('a'))

print("Reversed string: ", txt[::-1])