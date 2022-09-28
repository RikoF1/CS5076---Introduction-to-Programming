"""
Exercise 1
Write a function that receives a string as a parameter and returns the text in the string without vowels.
"""
user_input = list(input("Input a string here: "))
# user_input = list('I do not like vowels!')
letters = ["a", "e", "i", "o", "u"]
# print(user_input)

for letters in user_input:
    if "a" in user_input:
        user_input.remove("a")
    elif "e" in user_input:
        user_input.remove("e")
    elif "i" in user_input:
        user_input.remove("i")
    elif "o" in user_input:
        user_input.remove("o")
    elif "u" in user_input:
        user_input.remove("u")

print(' '.join(user_input))

"""
Exercise 2
Write a fucntion that receives a string that is a series of digits and returns the sum of all these digits
sumDigits("234") -> 9
"""
user_input = input("Input a series of digits here: ")

def sum_digit_string(string):
    sum_digit = 0
    for x in string:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z
    
    return sum_digit
        
print(sum_digit_string(user_input))

"""
Exercise 3
Using the function only_pos as a guide, write a function only_even that takes a list of integers and filters outthe odd values
"""
t = [1,2,3,4,5,6,7,8,9]
def only_even(lst):
    result = []
    for s in lst:
        if s % 2 == 0:
            result.append(s)
    return result

print(only_even(t))

"""
Exercise 4
Function to print out the three times table as a list (ending with 36).
Then modify your function to take a number as input and then print out its time stable (ending with 12 * number).
"""
# multiplier = 0
table_list = []

# for x in range(1, 13):
#     result = 3 * x
#     table_list.append(result)
#     print(f'3 times {x} is {table_list[x-1]}')

# take input
multiplier = int(input("Input integer here: "))

for x in range(1, 13):
    result = multiplier * x
    table_list.append(result)
    print(f'{multiplier} times {x} is {table_list[x-1]}')

"""
Exercise 5
Write a function that receives a list of umber as parameter and prints each number, its square and quare root.
You have to use a loop and the math library to get the sqrt function.
"""
# import libraries
import math
numbers = [18, 25, 3, 88, 60, 22, 89, 99, 20, 150]
y = len(numbers) # find the length
# print(y) # debug

def number_calculation(list):
    for x in range(y):
        print(f'The number on the list is {list[x]}, its square {list[x]**2} and its square root {math.sqrt(list[x]):.4f}.')
        # print(list[x])
        # print(list[x]**2)
        # print(math.sqrt(list[x]))
        
number_calculation(numbers)

"""
Exercise 6
Test out the following function
"""
text = "Hello World."
def printDown(text):
    i = 0
    while i < len(text):
        char = text[i]
        print(char)
        i+=1

printDown(text)

def printUp(text):
    i = len(text)
    while i > 0:
        char = text[i-1]
        print(char)
        i-=1

printUp(text)

"""
Rewrite printDown using a for loop
"""

def printDownLoop(text):
    i = 0
    length = len(text)
    for i in range(length):
        char = text[i]
        print(char)
        i+=1

printDownLoop(text)

"""
Exercise 7
Write 2 functions:
    head that returns the first element of a string
    tail that returns all of the string except the first element
"""
string = "Brookes"

def head():
    print(string[0])

def tails():
    print(string[1:])

head()
tails()

"""
Exercise 8
"""
total = 0
total_list = []

for x in range(65):
    total = (2 ** x) - 1
    total_list.append(total)
    print(f'In square {x} the grain total is {total_list[x]}')

print(total)
print(total_list)