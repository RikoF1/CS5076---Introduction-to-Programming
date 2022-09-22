#Functions
# Exercise 1
def mysteryNumber(x):
    x=x*x
    print("The value of x is now", x)

x = 2
print("Value of x is", x)
mysteryNumber(x)
print("The value of x after calling mysteryNUmber is:", x) # 2 as thought

# Exercise 2
n = int(input("Input here the value of n: "))
a = float(input("Enter here the value of a: "))
b = float(input("Enter here the value of b: "))
c = float(input("Enter here the value of c: "))

def checkFermat(n):
    if n > 2:
        if (a**n + b**n) == (c**n):
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work.")
    else:
        print("No, it only works if n > 2.")

checkFermat(n)

# Exercise 3
day_input = int(input("Type the day: "))
month_input = int(input("Type the month: "))
year_input = int(input("Type the last two numbers of the year: "))

def magic_date(x):
    if (x == (day_input * month_input)):
        print("This is a true magic date!")
    else:
        print("This is not a magic date.")

magic_date(year_input)

# Exercise 4

value1 = float(input("Input value 1 here: "))
value2 = float(input("Input value 2 here: "))
value3 = float(input("Input value 3 here: "))

input_list = [value1, value2, value3]

def median(lst):
    lst.sort()
    print(lst[1])

median(input_list)

# or

# Exercise 4
value1 = float(input("Input value 1 here: "))
value2 = float(input("Input value 2 here: "))
value3 = float(input("Input value 3 here: "))

def median(a, b, c):
    if ((a > b) and (b > c)) or ((c > b) and (a < b)):
        print(b, "is the median value.")
    elif ((b > a) and (a > c)) or ((c > a) and (a > b)):
        print(a, "is the median value.")
    else:
        print(c, "is the median value.")

median(value1, value2, value3)

# a > b > c
# a > c > b
# b > a > c
# b > c > a
# c > a > b
# c > b > a