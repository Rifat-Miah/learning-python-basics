# Reading Files:
# 1) Read entire file: 
#    with open("fileName.txt","r") as f:
#         data = f.read()
#         print(data)

file = open("practice2.txt", "r")
data = file.read()
print(data)
file.close()       # when we use "with" keyword not required to close()

with open("practice2.txt", "r") as f:
    data = f.read()
    print("File Data: ", data)


# 2) Read line by line
with open("practice4.txt", "r") as f2:
    line1 = f2.readline()
    print("Line 1 : ", line1)
    line2 = f2.readline()
    print("Line 2 : ", line2)

    line3 = f2.readline()
    print("Line 3 : ", line3)
    line4 = f2.readline()      # empty because it file has 3 lines
    data = f2.read()           # empty
    print("Line 4 : ", line4)
    print("Data: ", data)