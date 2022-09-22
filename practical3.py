# Exercise 1 - Write a program that given the total amount on the receipt and the number of items, it displays thefinal amount to pay.

input_amount = float(input("Input here the total amount on the receipt: "))
input_items = int(input("Input here total of items on the receipt: "))

if input_items < 10:
    print(input_amount)
elif input_items < 20:
    print(input_amount * 0.80)
elif input_items < 30:
    print(input_amount * 0.70)
else:
    print(input_amount * 0.50)

# Exercise 2 - Write a program that reads a letter from the English alphabet from the user. If a,e,i,o,u = vowel, if y = sometimes vowel sometimes not, else = consonant

input_letter = input("Input here one letter from the English alphabet: ")

if (input_letter == 'A') | (input_letter == 'a') | (input_letter == 'E') | (input_letter == 'e') | (input_letter == 'I') | (input_letter == 'i') | (input_letter == 'O') | (input_letter == 'o') | (input_letter == 'U') | (input_letter == 'u'):
    print("The letter", input_letter, "is a vowel.")
elif (input_letter == 'Y') | (input_letter == 'y'):
    print("The letter", input_letter, "can sometimes be a vowel, sometimes a consonant")
else:
    print("The letter", input_letter, "is a consonant.")

# Exercise 3 - Write a program that asks the user for the length and width of two rooms. It should then inform theuser to say whether the areas are the same, or if not, which room is bigger.

length_input1 = float(input("Input the length of room 1 here: "))
width_input1 = float(input("Input the width of room 1 here: "))
length_input2 = float(input("Input the length of room 2 here: "))
width_input2 = float(input("Input the width of room 2 here: "))

area_room1 = length_input1 * width_input1
area_room2 = length_input2 * width_input2

if area_room1 == area_room2:
    print("The area of the rooms are the same")
elif area_room1 > area_room2:
    print("Room 1 has a greater area.")
else:
    print("Room 2 has a greater area.")

# Exercise 4 - Write a program that reads the name of a month from the user as a string. Then displays the number of days in that month.

month_list = ["January", "March", "May", "July", "August", "October", "December"]

month_input = input("Input a month here to know how many days it has: ")
month_input = month_input.capitalize()

if month_input in month_list:
    print(month_input, "has 31 days.")
elif month_input == "February":
    print(month_input, "has 28 or 29 days, depending on the year.")
else:
    print(month_input, "has 30 days.")