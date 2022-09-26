"""
program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit.
Should nclude rows for all temperatures between 0 and 100 degrees Celsisus that are multiples of 10 degrees Celsius.
"""

for celsius in range(0,101,10):
    fahrenheit = (celsius * 1.8) + 32
    print(f'{celsius:.0f} Celsius is the equivalent temperature to {fahrenheit:.0f} Fahrenheit.')