def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The GCD of a and b, or None if inputs are invalid.
    """
    # Non-integer inputs
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None
    
    # Handle negative numbers
    a, b = abs(a), abs(b)
    
    # Base case: if b is 0, return a
    if b == 0:
        return a
    
    return gcd(b, a % b)

#Some Test Cases
print(gcd(48, 18))          # Output: 6
print(gcd(17, 5))           # Output: 1 
print(gcd(-36, 24))         # Output: 12 
print(gcd(0, 23))           # Output: 23 
print(gcd(0, 0))            # Output: 0 
print(gcd(123456, 7890))    # Output: 6 
print(gcd(3.14, 2))         # Output: Error: Both inputs must be integers. None
print(gcd("a", 2))          # Output: Error: Both inputs must be integers. None