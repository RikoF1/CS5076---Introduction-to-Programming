"""
Lecture 5 powerpoint exercises
"""

for j in range(5):
    print("I love python!", j)

total = 0

for i in range(5):
    num = int(input("Input number here: "))
    total = total + (num**2)    

print(total)

for j in range(5,101):
    if j % 5 == 0:
        print(j)

# or if you assume it is a multiple of 5

for k in range(5, 101, 5):
    print(k)

name = "Rodrigo"

for letter in name:
    print(letter)

# while loop

    while True:
        print("I love python")

# example number = 0

number = 10

while number > 0:
    print(number)
    number = number - 1
# else:
#    print("finished")
print("finished")

# generate random integer values
import random
from random import seed
from random import randint

#global variable

# my try
# for random_number in range(randint(1,10)):
#     # local variables
#     number_user = int(input("Input here the number: "))

#     if number_user > random_number:
#         print("Lower")
        
#     elif number_user < random_number:
#         print("Higher")
        
#     else:
#         print("Bang on!")
#         exit   

# teacher

number = random.randint(1,10)
guess = int(input("Please enter a number between 1 and 10: "))

while guess != number:
    if guess < number:
        print("Your guess is too low.")
        guess = int(input("Please enter a number between 1 and 10: "))
    else:
        print("Your guess is too high.")
        guess = int(input("Please enter a number between 1 and 10: "))

print("Congratulations you guessed the number.")

# num = 30
for i in range(1,100):
    if i > 10 and i < 50:
        continue
    print("Current number is", i)
    
"""
Write a for loop that print out the integers 2 through 10, each on a new line, by using the range() fucntion
"""

for i in range(2,11):
    print(i)

"""
Use a while loop that prints out the int 2 throught 10
"""

a = 2
while a < 10:
    a = a + 1
    print(a)