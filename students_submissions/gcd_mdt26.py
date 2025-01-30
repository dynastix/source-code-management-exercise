def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    if (b > a):
        x = a
        a = b
        b = x
    r = a%b
    if (r == 0):
        return b
    else:
        return gcd(b, r)
#    pass
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
