"""
Write a program that asks the user for an element and checks whether an element exists in the list employing binary seach.
a) First create a function that asks the user for the number of elements in the list,
then populates the list wiht the number of elements specified by the user.
b) Create a function that sorts the list in part a).
c)  Write a function that asks the user for an element, and checks whether the element exists using binary search.
The function should display the appropriate message to the user.
"""
# libraries
import random

#global variables
list = []

# function to ask the user and populate list
def populateList(lst):
    # user element input
    user_element = int(input("Input the number of elements you want in the list: "))
    # i = 0
    for i in range(user_element):
        lst.append(random.randint(-100,100))
        # i += i
    return lst

def sortList(lst):
    lst.sort()
    return lst

def searchBinary(lst):
    user_elmnt_input = int(input("Input the element you want to find: "))
    low = 0
    high = len(lst) - 1
    pos = -1

    while low <= high and pos == -1:
        mid = (low + high) // 2
        if lst[mid] < user_elmnt_input:
            low = mid + 1
        elif lst[mid] > user_elmnt_input:
            high = mid - 1
        else:
            pos = mid
    if pos != -1:
        return f'The position of the wanted element is {pos}.'
    else:
        return '''The element you're looking for does not exist in the list.'''
   

# run time
populateList(list)

# sort the list
print(sortList(list))

print(searchBinary(list))