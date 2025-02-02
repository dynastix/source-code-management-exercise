def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
    """
    
    if type(a) != int or type(b) != int:
        print("Both inputs must be integers.")
        return None
    if b == 0:
        return a
    if a < 0: 
       a = abs(a)
    if b < 0:
         b = abs(b)
         
    return gcd(b, a%b)

# Test cases
print(gcd(120, 44))  # 4
print(gcd(-48, 18)) # 6
print(gcd(15, 135))  #15
print(gcd(0, 0)) # 0
print(gcd(-101, -10)) # 1
print(gcd(48, '18')) # error message
