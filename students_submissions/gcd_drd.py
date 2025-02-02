def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two positive integers using recursion.
    """
    # Error handling for negative inputs
    if a < 0 or b < 0:
        raise ValueError("Both inputs must be positive integers.")
    
    # Base cases for recursion
    if b == 0:
        return a
    if a == 0:
        return b
    
    # Recursive case
    return gcd(b, a % b)


# Test cases
print(gcd(54, 24))
print(gcd(48, 18))
print(gcd(101, 10))