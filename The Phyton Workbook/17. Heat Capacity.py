"""
Program that reads the mass of water and the temperature change from the user. 
Display the total amount of energy that must be added or removed to achieve the desired temperature change.
"""
# water_mass_input = float(input("Input here the mass of water: "))
# temp_change_input = float(input("Input here difference of temperature to achieve: "))
water_mass_input = 250 # metric cup
temp_change_input = 100 # delta 100 degrees

amount_energy = water_mass_input * 4.186 * temp_change_input

print("The total amount of energy that must be either added or removed to achieve the desired temperature is:", amount_energy, "joules.")

# Extend the program  to compute the cost of heating the water for a cup of coffee

jouleToKilowatt = amount_energy * 2.77777778e-7

electricity_cost = jouleToKilowatt * 8.9

print(amount_energy)
print(f'To boil water for a cup of coffee it will cost {electricity_cost:.2f} cents.')