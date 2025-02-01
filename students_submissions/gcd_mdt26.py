def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here

    #This tests if a == b
    if (a == b):
        print("NOTE: Entered integers are equal.")
        return a
    #This switches the inputs if the denominator is greater
    if (b > a):
        gcd(b, a)
    #This tests for inputs that are 0
    if (a == 0 or b == 0):
        print("ERROR: Neither input can be zeros.")
        return
    #This tests for negative inputs
    if (a < 0 or b < 0):
        print("ERROR: Neither input can be negative.")
        return
    #This tests for prime numbers in the parameters
    if (isPrime(a) and isPrime(b)):
        print("NOTE: Both integers are prime. Returning 1.")
        return 1
    #This tests if a (the dividend) is prime
    if (isPrime(a)):
        print("NOTE: Dividend is prime. Returning 1.")
        return 1

    #Seperates actual function from the function that checks the values
    #so that at each recurrence, it doesn't keep unecessarily checking.
    return gcd_funct(a, b)
#    pass

def gcd_funct(a: int, b: int) -> int:
    r = a%b
    if (r == 0):
        return b
    else:
        return gcd_funct(b,r)

#This function tests whether a number is prime
def isPrime(a: int) -> bool:
    if (a == 1):
        return False
    if (a == 2):
        return True
    sqrt_a = a ** 0.5
    i = 2
    while (i <= sqrt_a):
        if (a % i == 0):
            return False
        i += 1
    return True

#Testing purposes
print("a = ", end='')
a = int(input())
print('\nb = ', end='')
b = int(input())
print(f'\ngcd({a}, {b}) = {gcd(a,b)}')
