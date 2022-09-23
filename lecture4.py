def function_name(param1):
    print("hello world")
    return None

def add2(a,b):
    """
    This function is to sum up two values
    """
    c = a + b
    return c # no return outputs None

def add3(a,b,d):
    """
    This function is to sum up three values
    """
    c = a + b + d
    return c


sum = add2(2,3)
print(sum)

# Write a function cube() to return value inputed to raised of the third power.

def cube(num):
    cb = num ** 3
    return cb

cube_input = float(input("Input cube number here: "))

print(cube(cube_input))

# now for any power

def cube(num, pow):
    cb = num ** pow
    return cb

cube_input = float(input("Input cube number here: "))
power_input = float(input("Input power number here: "))

print(cube(cube_input, power_input))

# function greet() that displays text "Hello <name>!"

def greet(name):
    # print("Hello", name, "!")
    name = "Hello " + name +"!"
    return name

input_name = input("Input a name here: ")
# greet(input_name)
print(greet(input_name))