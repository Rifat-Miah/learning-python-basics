'''Write a Python function that takes an array of integers and 
returns the second largest element in the array. 
If the array contains fewer than two unique elements, return None.'''

def second_largest(arr):
    unique = list(set(arr)) # remove duplicate

    if len(unique) < 2:   # array contains fewer than two unique elements
        return None  
    
    unique.sort()  # sort ascending order

    return unique[-2]  # 2nd largest 

print(second_largest([10, 30, 20, 80, 40, 900]))
print(second_largest([5, 7, 5, 8]))
print(second_largest([10, 10, 10, 10]))
print(second_largest([7, 3, 88, 111]))
print(second_largest([-1, -3, -4, -9]))