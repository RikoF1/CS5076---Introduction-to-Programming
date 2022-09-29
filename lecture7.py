f = open("hello.txt")

# item = f.read()
# print(item)

# for c in item:
#     print(c)

# for line in f:
#     print(line)

# print(f.readline())

print(f.readlines())

f.close()

fh = open("file.txt", "w+") # ,"x" / "w" / "a" / "w+"
# fh.write("This is a new file.\n")
# fh.write("100\n")
# fh.write("Appendix")
print("This is a new file", file=fh)

fh.close()

import pandas as pd

x = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

df = pd.DataFrame(x, columns = ['col1', 'col2', 'col3'])
# df = pd.DataFrame(x)
df.to_csv("digits.csv") # can be index = False

csvFile = pd.read_csv('digits.csv', index_col = 0, skiprows = [])
print(csvFile)
print(csvFile.values.tolist())

# Exception and error handling

def div(x,y):
    try:
        return x / y
    except:
        print("There is an error.")
        return None

print(div(10,0))

def func():
    while True:
        try:
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            return x / y
            # break
        except:
            print("Your last input is not a number or Y is zero.")

print(func())

list = [1, '2', 3, 'c', 5]
nlist = []

for j in list:
    tmp = int(j)
    nlist.append(tmp)
print(nlist)