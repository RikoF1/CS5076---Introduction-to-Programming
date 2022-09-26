"""
Exercise 1
Input 20 numbers, at the end show the total.
"""
total = 0
for x in range(1,21):
    user_input = int(input("Input a number here: "))
    total = total + user_input
else:
    print("The number total is:", total)

"""
Exercise 2
Calculate 1p saving challenge
"""
total = 0
for day in range(365):
    day = day + 1
    total = day + total
    print(f'{total * 0.01:.2f} pounds.') # * 0.01 to transform p in pounds.

"""
Exercise 3
Write a program that displays all the numbers multiple of 3 up to 300 using range with 3 parameters.
"""
x = 0
while x in range(0,301,1):
    x = x + 1
    if x % 3 == 0:
        print(x)

# or
for x in range(0,301,3):
    print(x)

"""
Exercise 4
Program that asks the user for a set of positive numbers and identifies the highest among them.
The user enters the number 0 to finish the sequence. You have to implement the algorith and test it.
"""
number_input = int(input("Input number here: "))
highest = number_input

while number_input != 0:    
    if number_input > highest:
        highest = number_input
    number_input = int(input("Input number here: "))
print(highest)

"""
Exercise 5
Record the temperature records for 7 days.
Write a program that allows the user to input the temperature and when the loop is finished, display the average temp for the week.
"""
week_temp = 0
week = 0
while week < 7:
    temp_input = float(input("Input Temp: "))
    week += 1
    week_temp = week_temp + temp_input

print(f'The average week temperature was {(week_temp/7):.2f} degrees.')

"""
Exercise 6
Running on a treadmill constant speed burns 9.7 calories per minute.
Write a program that uses a loop  to display the number of calories burned after 10, 15, 20, 25 and 30 minutes.
"""

for minutes in range(10,31,5):
    print(f'In {minutes} minutes you burned {(minutes * 9.7):.2f} calories.')