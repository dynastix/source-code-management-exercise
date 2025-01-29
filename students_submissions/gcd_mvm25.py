def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Inputs must be integers.")
        return None
    
    if a == 0 and b == 0:
        print("Error: GCD is undefined for both values being zero.")
        return None
    
    # Ensure the numbers are positive for computation
    a, b = abs(a), abs(b)
    
    # Base case of recursion
    if b == 0:
        return a
    return gcd(b, a % b)

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1