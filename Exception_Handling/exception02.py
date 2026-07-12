# File Not Found
filename = "missing_file.txt"

try:
    with open(filename, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Please check the filename and path.")