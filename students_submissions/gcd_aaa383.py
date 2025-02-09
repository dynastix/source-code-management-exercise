def gcd(a: int, b: int) -> int:
    
    if not isinstance(a, int) or not isinstance(b, int):
        print('Error: Both arguments must be integers')
        return None
    a=abs(a)
    b=abs(b)
    
    if b==0:
        if a==0:
            print("Error: GCD of 0,0 is undefined")
            return None
        return a
    return gcd(b, a%b)

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(0,0))  # Expected output: Error: GCD of 0,0 is undefined, Return: None
print(gcd(10, 'a'))  # Expected output: Error: Both arguments must be integers, Return: None