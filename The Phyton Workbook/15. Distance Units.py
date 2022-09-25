"""
Program that reads measurement in feet from user. Displays equivalent distance in inches, yards and miles.
"""
# user input
feet_input = float(input("Input here distance in feet: "))

# conversion
feetToInch = feet_input / 12
feetToYard = feet_input * 1/3
feetToMile = feet_input * 0.0001893939

print(f'The equivalent distance in inches is {feetToInch:.3f} inches, {feetToYard:.3f} yards and {feetToMile:.3f} miles.')