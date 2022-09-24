"""
Reads value input done by the user, add the tax and output the tip and the total meal value in separate lines.
"""
meal_cost_input = float(input("Input the cost of the meal here: "))

meal_tax = meal_cost_input * 0.23

meal_tip = meal_cost_input * 0.18

print(f'The tax for the meal is: ${meal_tax:.2f}.\nThe meal tip is ${meal_tip:.2f}.\nTherefore the grand total of the meal is ${(meal_cost_input + meal_tax + meal_tip):.2f}.')