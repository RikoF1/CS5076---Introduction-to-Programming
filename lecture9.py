"""
primes exercise
"""
list = []

def is_prime(number):
    if number < 0:
        print("Invalid case.")
        return

    elif number == 0 or number == 1:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False  

    return True

def prime_list(number):
    for item in range(2, number+1):
        if is_prime(item) == True:
            list.append(item)
    






## runtime
# try:
#     num = int(input("Enter a number: "))
#     print(is_prime(num))
# except:
#     pass

try:
    num = int(input("Enter a number here: "))
    print(is_prime(num))
    print(list)
except:
    print("Provide a valid integer.")
