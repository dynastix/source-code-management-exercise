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
    #This tests for inputs that are 0
    if (a == 0 or b == 0):
        print("ERROR: Neither input can be zero.")
        return
    #This tests for negative inputs
    if (a < 0 or b < 0):
        print("ERROR: Neither input can be negative.")
        return
    #The following tests if either parameter is prime. If both are prime, algo returns 1
    a_isPrime = isPrime(a)
    b_isPrime = isPrime(b)
    if (a_isPrime and b_isPrime):
        print("NOTE: As both entered values are prime, the algorithm is returning 1.")
        return 1

    #The following executes the actual gcd seperately from the edge case checks so that
    #the prime check isn't executed at each recurrence.
    if (b > a):
        return gcd_er(b, a)
    else:
        return gcd_er(a, b)

#This function does the actual gcd operation.
def gcd_er(a: int, b: int) -> int:
    r = a%b
    if (r == 0):
        return b
    else:
        return gcd_er(b,r)

#This function tests whether a number is prime. If it is, it prints a message saying so.
def isPrime(a: int) -> bool:
    if (a == 1):
        return False
    if (a == 2):
        print(f'{a} is prime.')
        return True
    sqrt_a = a ** 0.5
    i = 2
    while (i <= sqrt_a):
        if (a % i == 0):
            return False
        i += 1
    print(f'{a} is prime.')
    return True

#Testing
print("a = ", end='')
a = int(input())
print('b = ', end='')
b = int(input())
print(f'gcd({a}, {b}) = {gcd(a,b)}')
