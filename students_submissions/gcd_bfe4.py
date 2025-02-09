def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None
    if a == 0 and b == 0:
        print("Error: GCD is undefined for (0, 0).")
        return None
    a, b = abs(a), abs(b)
    return a if b == 0 else gcd(b, a % b)

print(gcd(48, 18))
print(gcd(101, 103))
print(gcd(-48, 18))
print(gcd(0, 18))
print(gcd(0, 0))
print(gcd("a", 18))
