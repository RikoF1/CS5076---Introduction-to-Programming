"""
Program that reads two integers, a and b. And display:
sum of a and b
The difference when b is subtracted from a
The product of a and b
The quotient when a is divided by b
The remainder when a is divided by b
The result of log10 a
The result of a^b
"""
# import math library
import math

# user input values
a = int(input("Enter an integer number a here: "))
b = int(input("Enter an integer number b here: "))

print("The sum of a and b is:", a + b)
print("The difference when b is subtracted from a is:", a - b)
print("The product of a and b is:", a * b)
print("The quotient when a is divided by b is:", a // b)
print("The remainder when a is divided by b:", a % b)
print("The result of log10 a", math.log10(a))
print("The result of a^b is:", a**b)