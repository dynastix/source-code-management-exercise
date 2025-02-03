def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Error cases
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: all inputs must be integers")
        return None
    if (a == 0) and (b == 0):
        print("Error: Both numbers can't be 0")
        return None
    if (a < 0) or (b < 0):
        print("Error: No negatives")
        return None
    
    # Base case
    if b == 0:
        return a
    return gcd(b, a%b)

# test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1

print(gcd(10.5, 5))       # Expected: Error message & None
print(gcd("12", 6))       # Expected: Error message & None
print(gcd([4, 8], 2))     # Expected: Error message & None
print(gcd(0, 0))    # Expected: None (Undefined)
print(gcd(-9, 27))  
