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

    r = a%b
    if (r == 0):
        return b
    else:
        return gcd(b, r)
#    pass

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

#TESTS
#print(gcd(54, 24))  # Expected output: 6
#print(gcd(24, 54))  # Expected output: 6, same as above
#print(gcd(48, 18))  # Expected output: 6
#print(gcd(101, 10))  # Expected output: prints a note, and 1
#print(gcd(100, 0)) # Expected output: prints error message
#print(gcd(100, -2)) # Expected output: prints error message
#print(gcd(100,100)) # Expected output: prints a note indicating equality
#print(gcd(21, 4)) # Expected output: 1
#print(gcd(100,5)) # Expected output: 5
