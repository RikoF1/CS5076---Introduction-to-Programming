"""
Convert MPG to L/100km
"""
mpg_input = float(input("Input mpg value: "))

mpgToKml = 235.21 / mpg_input

print("The fuel effiency is of:", mpgToKml, "L/100km")