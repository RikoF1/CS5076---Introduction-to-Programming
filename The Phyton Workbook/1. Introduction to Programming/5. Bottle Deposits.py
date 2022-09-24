"""
Receives how many bottles of different sizes the user has and calculates how much deposit the user will receive back when recycling them.
"""
# Global Variables
small_bottle = 0.10
big_bottle = 0.25

# User input Variables
small_bottle_input = int(input("Input here how many bottles with less than 1 litre you will be recycling: "))
big_bottle_input = int(input("Input here how many bottles with more than 1 litre you will be recycling: "))

refund_total = (small_bottle * small_bottle_input) + (big_bottle * big_bottle_input)

print(f'You will be receiving a total of ${refund_total:.2f} for recycling those bottles.')