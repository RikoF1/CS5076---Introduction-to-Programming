
print("Hello World")

print("Hello")

# exercise 1
print("I love Python!")

# exercise2
x = "Yellow"

print(x)
# exercise2.1

bb = 5
print(bb)

# exercise 2.2
aa = 10
print(aa+bb)
print(aa*bb)
print(aa/bb)

## console needed
type(10) # int
type("10") # string
"this is python"


# exercise 3
# name = input("Enter your Name:")
name = input("Enter your name:")
age = input("Enter your Age:")

agecalc = 100 - int(age)
yearcalc = agecalc + 2022

print(name + " you will be 100 years old in " + str(yearcalc))

# exercise 4
# printable = name + " you will be 100 years old in " + str(yearcalc) #debug only

# for i in range(5):
#    print(name + " you will be 100 years old in " + str(yearcalc))

# exercise 5
repeatmanytimes = input("How many times you want it to repeat?") # change the order if necessary to have inputs before displaying anything

for i in range(int(repeatmanytimes)):
    print(name + " you will be 100 years old in " + str(yearcalc)) 