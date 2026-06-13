# Open a file called practice2.txt in write mode.

file = open("practice2.txt", "w")
file.write("1. 'w' mode opens the file for writing (overwrites existing content if the file already exists).\n")
file.write("2. write() method adds new text to the file.\n")
file.write("3. When using with, the file closes automatically at the end of the block.")
