def gcd(a: int, b: int) -> int:
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)

# Test cases
print(gcd(54, 24))
print(gcd(48, 18))
print(gcd(101, 10))
print(gcd(-48, 18))
print(gcd(0, 0))