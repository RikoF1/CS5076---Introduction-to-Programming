"""
Write a function that takes a list of values and an non-negative integer, n, as its parameters.
The function should return a copy of the list as the only result. The order of the elements does not have to match the order on the original
Write a main program that demonstrates your function.
Function should read a list of numbers from the user and remove the two largest and two smallest values from it.
Display the list with the outliers removed, followed by the original list.
A error should be shown if less than 4 values are input.
"""
# list = [5, 2, 3, 4, 5, 6, 7, 1, 9]

def new_list(lst, n): # n needs to be int positive
    l = len(lst)
    s = l - n
    lst.sort()
    new_lst = lst.copy()
    new_lst = new_lst[n:s]
    print(f'This is the new list: {new_lst}')
    print(f'This is the old list: {lst}')

"""
Main program
"""
# global variables
x = 2 # numbers to remove
user_list = [] # starting list
#user input values
user_input = input("Input here data to add to a list: ")

while len(user_list) < 4:
    if user_input != "":
        user_list.extend(user_input)
        user_input = input("Input here data to add to a list: ")
    else:
        print("You must have at least 4 values in the list.")
        user_input = input("Input here data to add to a list: ")
else:
    while user_input != "":
        user_list.extend(user_input)
        user_input = input("Input here data to add to a list: ")
    else:
        new_list(user_list,x)