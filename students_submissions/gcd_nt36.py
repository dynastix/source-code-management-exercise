def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if a < 0 or b < 0:
        return None
    
    if a == 0:
        return b
    
    if b == 0:
        return a
    
    if a == b:
        return a
    
    if a > b:
        return gcd(b, a % b)
    
    if b < a:
        return gcd(a, b % a)