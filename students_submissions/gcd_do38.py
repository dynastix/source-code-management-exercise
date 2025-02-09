def gcd( a: int, b: int ) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None
    
    if a == 0 and b == 0:
        print("Error: GCS is undefined for (0, 0).")
        return None
    
    a, b = abs(a), abs(b)

    if b == 0:
        return a
    
    return gcd(b, a % b)


# Test Cases
print(gcd(54, 24)) # Expected output: 6
print(gcd(48, 18)) # Expected output: 6
print(gcd(101, 10)) # Expected output: 1