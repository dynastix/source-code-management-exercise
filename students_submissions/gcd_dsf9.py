def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if a < 0 or b < 0:
        print("Error: Negative Input\na: {}, b: {}".format(a,b))
        return None;
    if b == 0:
        return a;
    return gcd(b, a % b);

# Test cases
print(gcd(107, 214)) # Expected output: 107
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(124, 23)) # Expected output: 1
print(gcd(124, 31)) # Expected output: 31