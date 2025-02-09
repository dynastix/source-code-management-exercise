def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    if b == 0:
        return a
    return gcd(b, a % b)

# Test cases
print(gcd(24, 54))
print(gcd(18, 48))
print(gcd(100, 10))
print(gcd(10, 100))