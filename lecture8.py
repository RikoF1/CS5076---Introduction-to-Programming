"""
Given a mixed type list of n elements including string and numbers, write a function to search a given element x in the list.
"""
# global variables
list = ["hello", 2, 3, "world", 4, 6]
target = "world"

def lin_search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return "Not in the list"

print(lin_search(list, target))

"""
Write a program to find the square root of 'x' using the binary search algorithm. 
If 'x' is not a perfect square, return the floor of the square root.
"""
def binary_search(x):
    low = 0
    high = x
    while True:
        mid = (low + high)//2
        if mid**2 == x:
            return mid
        elif x < mid ** 2:
            high = mid
        if high - low <= 1:
            if high == low:
                return low
            else:
                h1 = abs(high ** 2 - x)
                l1 = abs(low ** 2 - x)
                if h1 < l1:
                    return high
                else:
                    return low

print(binary_search(70))

"""
Write a program that 'bubble sorts' into non-descending order an array of size 20 filled with random integers.
Print out the array at the beginning and after every excahgne of the neightbouring elements.
This will enable you to see the bubbling and will also help with debugging.
"""
