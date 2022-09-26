"""
Duck brother's exercise
"""
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

"""
 Do Breonna trailer exercise
"""

"""
String Slices
"""

mySlice = "Monty Python"
print(mySlice[0:5])
print(mySlice[6:12])
print(mySlice[:3])
print(mySlice[3:])
print(mySlice[-3:])
print(mySlice[:-3])
print(mySlice[:])

"""
Strings are immutable
"""
greeting = "Hello, World!"
# greeting[0] = "J" # error

new_greeting = "J" + greeting[1:]
print(new_greeting)

"""
Looping and counting
"""

word = "Natalie Wynn"
count = 0

for letter in word:
    if letter == "n" or letter == "N":
        count = count + 1
print(count)