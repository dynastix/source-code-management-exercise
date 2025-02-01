def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """

    if a < 0:
        raise ValueError("Please input a positive number for 'a'")
    if b < 0:
        raise ValueError("Please input a postive number for 'b'")
    
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
    

    
    pass

#Test Cases:
print(gcd(54, 24))
print(gcd(48, 18))
print(gcd(101, 10))