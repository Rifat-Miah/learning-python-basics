# Write a program to read a text from a given file practice1.txt
# and find whether it contains the word 'automate'

file = open("practice1.txt", "r")
dataOfFile = file.read()

dataOfFile = dataOfFile.lower()
if "automate" in dataOfFile:
    print("Yes, automate word is present this file.")
else:
    print("Automate word is not available this file.")