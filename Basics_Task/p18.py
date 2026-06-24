# Print all the even numbers between 0 to 100 usig for and range

count = 0

for i in range(0, 101, 2):
    print(i, end=" ")
    count += 1

    if count % 10 == 0:
        print()
print("Total even numbers printed = ", count)