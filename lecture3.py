x1 = int(input("X value for point 1: "))
y1 = int(input("Y value for point 1: "))
x2 = int(input("X value for point 2: "))
y2 = int(input("Y value for point 2: "))

import math
distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

print(distance)

# "lecture 3"

lecture3 = "LEcturE3"
print(lecture3.upper())
print(lecture3.capitalize())
print(lecture3.lower())

# Enter a number
a = int(input("Enter a number: "))
if a > 2:
    print("This number is bigger than two.")
else:
    print("This number is not bigger than two.")

# time to go gym or home

b = int(input("Enter a number: "))

if b > 19:
    print("Go to the gym.")
else:
    print("Go home.")

# Example 
# Write a program that asks the user for the temperature of water and it displays as a result the state of the water (e.g. liquid, gas, ice).

temp = int(input("Input water temperature here (celsius): "))

if temp < 0:
    print("Ice state.")
else:
    if temp >= 100:
        print("Gas state.")
    else:
        print("Liquid state.")

# Lecture exercises
# 1. Write a code with a Syntax error

#Print("hello")

# Runtime error

# print("hello")
# print(c)
# print("world")

# Semantic error
    # want multiplication
# print(a + b) 

# 2. Exponential notation

d = 1000000000
d = 1e9
d = 10**9

# 3. Write exponent.py script that asks for a input of the user of two numbers, number1 power of number2
number1 = float(input("Input number 1 here: "))
number2 = float(input("Input number 2 here: "))

print(number1**number2)

# 5. Write a program to convert (user input) degree to radian.
# π/180

degrees = float(input("Input number of degrees here: "))
radian = degrees*(math.pi/180)
print(radian)

# True or false

a = (1 <= 1) and (1 != 1)
b = not (1 != 2)
print(a)
print(b)

# Write a script that prompts the user to enter a word using the input()

word = input("Input a word here: ")

if len(word) == 5:
    print("The word has 5 characters.")
elif len(word) > 5:
    print("The word has more than 5 characters.")
else:
    print("The word has less than 5 characters.")