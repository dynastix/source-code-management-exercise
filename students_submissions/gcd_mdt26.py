def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here

    #This switches the inputs if the denominator is greater
    if (b > a):
        x = a
        a = b
        b = x
    #This tests for inputs that are 0
    if (a == 0 or b == 0):
        print("ERROR: GCD algorithm can't work with zeroes.")
        return
    #This tests for negative inputs
    if (a < 0 or b < 0):
        print("ERROR: GCD algorithm can't work with negatives.")
        return

    r = a%b
    if (r == 0):
        return b
    #Tests for 1, indicating a prime number, but unclear if we need to point out which
    #input is prime
    #elif (r == 1):
        #print("NOTE: greater input value is prime.")
        #return r 
    else:
        return gcd(b, r)
#    pass

print(gcd(54, 24))  # Expected output: 6
print(gcd(24, 54))  # Expected output: 6, same as above
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(100, 0)) # Expected output: prints error message
print(gcd(100, -2)) # Expected output: prints error message
