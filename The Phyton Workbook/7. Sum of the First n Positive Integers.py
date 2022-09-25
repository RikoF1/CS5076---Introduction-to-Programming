"""
Program that reads positive integer n from user and displays the sum of all of the integers from 1 to n.
"""
integer_input = int(input("Input here a positive integer: "))

sum_integers = ((integer_input) * (integer_input + 1)) / 2

print("The sum of all integers from 1 to", integer_input, "is", int(sum_integers), ".")