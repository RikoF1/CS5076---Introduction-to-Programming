"""
Program to determine how much change to provide when the shopper pays for a purchase in cash.
pennies = 1
nickels = 5
dimes = 10
quarters = 25
loonies = 1
toonies = 2
"""
# Global Variables
cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarter = 25
cents_per_dime = 10
cents_per_nickel = 5
cent = 1

cents_total = int(input("Input the total of cents that you'll receive: "))

# Calculate minimum amount of coins for change

minimum_toonies_floor = (cents_total // cents_per_toonie)
minimum_toonies_remainder = (cents_total % cents_per_toonie)

minimum_loonies_floor = (minimum_toonies_remainder // cents_per_loonie)
minimum_loonies_remainder = (minimum_toonies_remainder % cents_per_loonie)

minimum_quarter_floor = (minimum_loonies_remainder // cents_per_quarter)
minimum_quarter_remainder = (minimum_loonies_remainder % cents_per_quarter)

minimum_dime_floor = (minimum_quarter_remainder // cents_per_dime)
minimum_dime_remainder = (minimum_quarter_remainder % cents_per_dime)

minimum_nickel_floor = (minimum_dime_remainder // cents_per_nickel)
minimum_nickel_remainder = (minimum_dime_remainder % cents_per_nickel)

# minimum_cent_floor = (minimum_nickel_remainder // cent)

print(f"You'll get back {minimum_toonies_floor} toonie(s), {minimum_loonies_floor} loonie(s), {minimum_quarter_floor} quarter(s), {minimum_dime_floor} dime(s), {minimum_nickel_floor} nickel(s) and {minimum_nickel_remainder} cent(s).")