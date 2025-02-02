def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    #base case
    if (a < 0 or b < 0):
        return 0
    if (b == 0):
        return a
    #recursive case
    else:
        #gcd of a,b = gcd of b,a%b
        c = a%b
        return gcd(b, c)

print("0, 0, gcd: ", gcd(0,0))
print("1, 2, gcd: ", gcd(1,2))
print("5, 20, gcd: ", gcd(5,20))
print("6, 18, gcd: ", gcd(6,18))
print("12, 8, gcd: ", gcd(8,12))
print("-12, 8, gcd: ", gcd(-12,8))
