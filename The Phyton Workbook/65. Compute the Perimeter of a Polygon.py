"""
Program that computes the perimeter of a polygon.
Begin by reading the x and y values for the first point on the perimeter from the user.
Then continue reading pairs of xand y values until a blank line is used for the x-coordinate.
Each time you read an additional coordinate, you should compute the distance to the previous point and add it to the perimeter.
When a blank line is entered the program should add the distance from the last point back to the first point.
Then, it should display the total perimeter.
"""
import math
# user input
x_coordinate_input = input("Input X coordinate here (blank to end): ")
x_perimeter = 0
y_perimeter = 0

while x_coordinate_input != "":
    y_coordinate_input = input("Input Y coordinate here: ")
    x_perimeter = float(x_coordinate_input) + float(x_perimeter)
    y_perimeter = float(y_coordinate_input) + float(y_perimeter)
    x_coordinate_input = float(input("Input X coordinate here (blank to end): "))

final_perimeter = math.sqrt((x_perimeter ** 2) + (y_perimeter ** 2))
print(final_perimeter)
