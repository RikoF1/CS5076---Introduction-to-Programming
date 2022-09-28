"""
create list
"""

lst = [1,2,3,4]
lst_str = ["a","hello", "python"]
# or
sublst = [1,2,3]
lst1 = [1, "strs", [1,2,3], sublst] # sublist, strings, numbers, etc

print(lst)

print(lst[0:2]) 

lst2 = [i for i in range(0,10)]

print(lst2[0:10:3]) # lst2[start:stop:step]


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

# for loop help
st = ["hello", "1", "world"]

for i in range(len(st)):
    st[i]

for i in st:
    print(i)