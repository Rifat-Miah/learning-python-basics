# for best practice use "try" and "except"
# if use this, when file not fount the system cannot crash 

import os 

try:
    with open("practice6.txt", "r") as f:
        lines = f.readlines()
        print("Output: ", lines)

except:
    print("This file does not exist.")