"""
Write a program that reads a radius (r) from the user. And compute and display the area of a circle with radius (r) and the volume of a sphere with radius (r).
"""
import math

radius_input = float(input("Input the radius (r) of the circle and sphere: "))

area_circle = math.pi * (radius_input) ** 2
sphere_volume = 4/3 * (math.pi) * (radius_input) ** 3

print(f'The area of the circle with radius {radius_input} is: {area_circle:.2f} cm2 and the sphere volume is: {sphere_volume:.2f} cm3.')