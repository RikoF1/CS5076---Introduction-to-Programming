## UNFINISHED ##
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
x_perimeter = 0
y_perimeter = 0
x_coordinate_input = input("Input X coordinate here (blank to end): ")
y_coordinate_input = input("Input Y coordinate here: ")
x_f_point = x_coordinate_input
y_f_point = y_coordinate_input

while x_coordinate_input != "":
    final_perimeter = ((x_perimeter) ** 2) + ((y_perimeter) ** 2)
    x_perimeter = math.sqrt((float(x_perimeter) - float(x_coordinate_input)) ** 2) 
    y_perimeter = math.sqrt((float(y_perimeter) - float(y_coordinate_input)) ** 2)
    x_coordinate_input = input("Input X coordinate here (blank to end): ")
    y_coordinate_input = input("Input Y coordinate here: ")

    # x_perimeter = math.sqrt((float(x_perimeter) - float(x_f_point)) ** 2)
    # y_perimeter = math.sqrt((float(y_perimeter) - float(y_f_point)) ** 2)
    # final_perimeter = ((x_perimeter) ) + ((y_perimeter) )
print(final_perimeter)
