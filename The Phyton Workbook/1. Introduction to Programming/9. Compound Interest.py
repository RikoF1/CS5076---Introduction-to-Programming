"""
App to calculate the money on an accoutn with 4% interest rate per year, on year 1, 2 and 3.
"""
starting_money = float(input("Input the amount of $ you will be starting with: "))

interest_rate1 = starting_money * 0.04
money_year1 = starting_money + interest_rate1

interest_rate2 = money_year1 * 0.04
money_year2 = money_year1 + interest_rate2

interest_rate3 = money_year2 * 0.04
money_year3 = money_year2 + interest_rate3

print(f'On year 1 you will have ${money_year1:.02f}\nOn year 2 you will have ${money_year2:.02f}\nOn year 3 you will have ${money_year3:.02f}.')