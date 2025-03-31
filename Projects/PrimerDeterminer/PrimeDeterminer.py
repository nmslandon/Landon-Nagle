import math;
number =int(input("Enter a number here to determine if it is prime: "))
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

if is_prime(number) == True: 
    print ("Your number is prime")
else: print ("Your number is not prime")