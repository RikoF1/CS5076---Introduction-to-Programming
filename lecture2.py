# Example 1: a car travels 120 miles in 10 hours. What is the speed of the car?

distance = 120
time = 10

speed = distance / time
print("The speed of the car is", speed, "miles per hour.")

# Example 2: a car travels 120 miles. What is the distance in KM?

travel = 120
km = 1.609344
travelling_distance = travel * km
print("The distance of 120 miles is", travelling_distance, "kilometres.")

# Example 3: improve example 1 to ask for the values from the user.

distanceInput = float(input("Input here the distance travelled in total:"))
timeInput = float(input("Input here the time taken on the travel:"))
print("The speed of the car is", distanceInput/timeInput , "miles per hour.")

# Example 4: improve example 1 to ask for the values from the user.

travelInput = float(input("Input here the distance in miles:"))

print(travelInput * km, "kilometres.")

# Example 5: write a program that converts the distance from km to miles.

kilometersInput = float(input("Input here the distance in kilometres:"))
mile = 0.621371192
print("The distance travelled was", kilometersInput * mile, "miles.")

# Example 6: write a program that asks the user for a temperature in Fahrenheit and convert it into Celsius.

tempFahrenheit = float(input("Input here the temperature in Fahrenheit:"))

tempCelsius = ((tempFahrenheit - 32)*5/9)

print(((tempFahrenheit - 32)*5/9), "degrees celsius.")

# print(tempCelsius, "degrees celsius.") # simpler way if doing various times

# Example 7: write a program where the user enters the gross salary and theprogram calculates the net salary by deducing 25% of taxes.

salaryInput = float(input("Input your gross salary here: "))

salaryAfterTaxes = salaryInput * 0.75

print(salaryAfterTaxes)

#debugging exercise
# This program calculates the retail price of an item

VAT = 0.017
item = input("Item description: ")
price = float(input("Item Price: "))

# Calculations

tax = price * VAT
price = price + tax

print("Item: ", item, "\nPrice after VAT is: ", price)
