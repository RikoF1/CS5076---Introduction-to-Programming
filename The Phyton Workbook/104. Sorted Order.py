"""
Program that reads integers from the user and stores them in a list.
Should continue reading values until the user enters 0.
Then, should display all the values entered by the user, except 0, in order from smallest to largest.
With one value appearing on each line.
"""
user_input = int(input("Input here integer values: "))
list = []

while user_input != 0:
    list.append(user_input)
    user_input = int(input("Input here integer values: "))

else:
    list.sort()
    length = len(list)
    x = 0
    while x in range(length):
        print(list[x])
        x += 1
