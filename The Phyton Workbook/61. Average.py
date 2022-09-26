"""
Program that computes the average of a collection of values entered by the user.
The user will enter 0 as a sentinel value to indicate that no further values will be provided.
Your program should display an appropriate error message if the first value entered by the user is 0.
"""
#user input variable
user_input = float(input("Input number here:"))

# global variables
collection = 0
number_entries = 0

while user_input != 0:
    collection = user_input + collection
    number_entries = number_entries + 1
    user_input = float(input("Input number here:"))

while user_input == 0 and collection == 0:
    print("You cannot choose 0 as the first number because it ends the value input indicator.")
    break

print(f'The average of the numbers is {(collection / number_entries):.2f}.')