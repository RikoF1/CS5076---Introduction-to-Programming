# exercise 1
firstname = input("What's your first name?")
lastname = input("What's your last name?")
age = input("What's your age?")
salary = input("What's your salary?")
postcode = input("What's your postal code?")

print("You're called " + firstname + " " + lastname + ", " + "you're " + age + " year's old." + '\n' + "You earn £" + salary + " per year and you live in " + postcode + ".")

# exercise 2
word = input("Write one word here:")
looping = float(input("How many times do you want it repeated:"))

print((word + '\n') * int(looping))

# exercise 3
number = int(input("Type a number here: "))
print(number)
print(number * 2)
print(number * 3)
print(number / 2)
# division with int and remainder
print(number // 3)
print(number % 3)

# exercise 4
ysalary = int(input("Input your yearly salary here: "))
print(ysalary / 12)
print((ysalary * 0.8) / 12)

# exercise 5
width = int(input("Type the width of the rectangle here: "))
height = int(input("Type the height of the rectangle here: "))
area = str(width * height)

print(area + " m2")

# exercise 6
side = int(input("Type the side of the square here: "))
area_sq = side * side
perimeter_sq = side * 4

print("The area of the square is: " + str(area_sq))
print("The perimeter of the square is: " + str(perimeter_sq))

# exercise 7
speed_light = 3E8 # per second
seconds_of_travel = int(input("Input here how many seconds you want the light to travel: "))
print(str(seconds_of_travel * speed_light) + " meters.")
print(str((seconds_of_travel * speed_light) / 1000) + " kilometers.")


miles = (((seconds_of_travel * speed_light) / 1000)* 0.621371192)

print(str(miles) + " miles.")

# exercise 8
feet = int(input("Input your feet here: "))
inches = int(input("Input your inches here: "))

conversion_m = (inches * 2.54) + (feet * 30.48)
print(conversion_m)