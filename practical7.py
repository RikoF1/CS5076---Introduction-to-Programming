"""
Exercise 1
"""
# libraries import
import random

# randomise number
numb1 = random.randint(0,999)
numb2 = random.randint(0,999)

sumRand = numb1 + numb2
# print(sumRand) # debug only

user_sum_input = int(input("Input what you think the sum is: "))

while user_sum_input != sumRand:
    print("Please try again.")
    user_sum_input = int(input("Input what you think the sum is: "))

else:
    print("Congratulations!")

"""
Exercise 2
"""
user_int_input = int(input("Input an integer value here: "))
lst = [2,3,4,5,6,-2,-4,-5,24]

while user_int_input != 0:
    lst.append(user_int_input)
    user_int_input = int(input("Input an integer value here: "))
# else:
#     nList = sorted(lst, key = lambda x: (x >= 0 > -x), reverse = True)
#     length = len(nList)

#     for i in range(length):
#         print(nList[i])
#         i += i

# or posList and negList ## NOT WORKING

else:
    posList = lst.copy()
    negList = lst.copy()
    posLength = len(posList)
    negLength = len(negList) 
    
    while posList[y] < 0:
        posList.remove(y)
        y += y

    while j > 0:
        negList.remove(j)
        j += j
    
## sort lists
posList.sort()
negList.sort()

"""
Exercise 3
Zoo determines the price of admission based on te age.
Guest 2 years or less = £0
Between 3 and 12 = £14
65 + = £18
Others £23
"""
# Global var
lst = []
user_input = input("Input the age of one of the guests here:")

while user_input != "":
    lst.append(int(user_input))
    user_input = user_input = input("Input the age of one of the guests here:")

else:
    listLength = len(lst)
    total = 0
    
    for x in range(listLength):
        if lst[x] >= 3:
            total = 14 + total
        elif lst[x] >= 13:
            total = 23 + total
        elif lst[x] >= 65:
            total = 18 + total
            
    print(f'The admission price for the group of guests is £{total:.2f}.')


"""Exercise 5"""
f = open("example.txt", "a")
f.write("\nThis is line 3\nThis is line 4")
f.close()

f = open("example.txt", "r")
print(f.read())
f.close()

"""
Exercise 6
Program that calculates the speed of a car, by asking the distance and the time from the user.
Should take into account errors that might happen as a reult of wrong inputs. Asking the user for correct values.
"""
# speed of car function

def speedOfCar(distance,time):
        speed = distance / time
        return speed
# program start runtime
distance_input = float(input("Input distance in metres: "))
time_input = float(input("Input distance in seconds: "))

try:
    speedOfCar(distance_input, time_input)
    print(f'The speed of the car is {speedOfCar(distance_input, time_input):.2f} m/s')
except:
    print("There is an error. Please input the right type of values.")
    distance_input = input("Input distance in metres: ")
    time_input = input("Input distance in seconds: ")