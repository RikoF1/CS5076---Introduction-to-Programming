"""
Gets two latitude and longitude points from earth and calculates the surface distance between them.
"""
# libraries import
import math
# user input variables

longitude1 = float(input("Input longitude of point 1: "))
latitude1 = float(input("Input latitude of point 1: "))

longitude2 = float(input("Input longitude of point 2: "))
latitude2 = float(input("Input latitude of point 2: "))

t1 = math.radians(latitude1)
g1 = math.radians(longitude1)
t2 = math.radians(latitude2)
g2 = math.radians(longitude2)

# formula of distance surface

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1-g2))

print(f'The distance between the two points of the earth following the surface is: {distance:.02f} km.')