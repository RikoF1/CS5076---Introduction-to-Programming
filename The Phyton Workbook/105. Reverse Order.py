"""
Program that reads integers from the user and stores them in a list.
Use 0 as sentinel value to mark the end of the input.
Once all the values have been read, the program should display them in reverse order. With one value per line.
"""
user_input = int(input("Input integer value here: "))
list = []

while user_input != 0:
    list.append(user_input)
    user_input = int(input("Input integer value here: "))

else:
    length = len(list)
    list.sort(reverse = True)
    for x in range(length):
        print(list[x])
        x += 1
