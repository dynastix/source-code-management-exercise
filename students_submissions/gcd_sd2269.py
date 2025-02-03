def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    
    # Base case
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
# Test Cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1

# test cases for prime numbers
print(gcd(7, 11))  # Expected output: 1
print(gcd(13, 17))  # Expected output: 1
print(gcd(19, 23))  # Expected output
