"""
Calculates the area of the Field
"""
length_input = float(input("Enter here the length of the field in feet: "))
width_input = float(input("Enter here the width of the field in feet: "))

area_field = length_input * width_input # area of the field

area_acre = (area_field / 43560) # converts squarefeet to acres

print("The farmer's field has an area of", area_acre, "acres.")