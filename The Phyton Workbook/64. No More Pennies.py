"""
program that reads prices from the user until blank line is entered.
Displays the total cost of all the entered items on one line
Followed by the amount due if the customer pays with cash on a second line.
The cash amount due should be rounded to the nearest nickel.
"""

price_input = input("Input price of item here: ")
total_cost = 0
while price_input != '':
    total_cost = float(total_cost) + float(price_input)
    price_input = input("Input price of item here: ")



# calculate nearest nickel
remainder_cost_cash = (total_cost * 100) % 5 # multiply 100 to get fractional values.
# total_cost_cash = total_cost
if remainder_cost_cash > 2.5:
    remainder_cost_cash = 5 - (remainder_cost_cash) 
    total_cost_cash = total_cost + (remainder_cost_cash / 100) # / 100 to get fractional value
else:
    remainder_cost_cash = 0 - remainder_cost_cash
    total_cost_cash = total_cost + (remainder_cost_cash / 100) # / 100 to get fractional value

# print output
print(f'Total cost of all items: ${total_cost:.2f}.') # total cost
print(f'Amount due if paying in cash: ${total_cost_cash:.2f}') # total cost for cash