def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None
    
    a, b = abs(a), abs(b)
    
    # If one number = 0, return the other if non-0
    if b == 0:
        if a != 0:
          return a
        else: return None
    
    return gcd(b, a % b)  # Recursive call
  
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
