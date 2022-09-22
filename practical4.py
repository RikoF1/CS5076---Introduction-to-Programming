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

def magic_date(year_input):
    if (year_input == (day_input * month_input)):
        print("This is a true magic date!")
    else:
        print("This is not a magic date.")

magic_date(year_input)

# Exercise 4
