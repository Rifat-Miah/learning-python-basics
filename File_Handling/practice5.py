# Read all lines 
with open("practice5.txt", "r") as f:
    readLinesMethod = f.readlines()
    print("Output: ", readLinesMethod)

# Print how many lines are present this files
    print("Number of lines in this file = ", len(readLinesMethod))