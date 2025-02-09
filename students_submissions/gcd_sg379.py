def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # The following solution returns the absolute value of the final
    # divisor to handle negative numbers and will return 0 if both inputs are 0

    if(type(a) != int or type(b) != int):
        print("Both a and b must be integer values")
        return None

    if(b == 0):
        return abs(a)
    
    return gcd(b, a%b)

print(gcd(101,10))
print(gcd(54,24))
print(gcd(24,54))
print(gcd(48,-18))
print(gcd(-18,48))
print(gcd(-48,-18))
print(gcd(15,0))
print(gcd(0,15))
print(gcd(0,0))
print(gcd(1.5,10))
