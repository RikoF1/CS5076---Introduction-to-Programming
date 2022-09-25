"""
Program that reads number of feet followed by number of inches and shows equivalent in centimeters
"""
#global variables
feet_input = int(input("Input here the number of feet: "))
inches_input = int(input("Input here the number of inches: "))

feetToCm = feet_input * 12 * 2.54
inchToCm = inches_input * 2.54

print(f'Your equivalent height is {(feetToCm + inchToCm):.2f} cm.')