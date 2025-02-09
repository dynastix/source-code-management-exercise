def gcd(a: int, b: int) -> int:
    if a == 0 and b == 0:
        print("ERROR: gcd of 0 and 0 is undefined.")
        return None
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    return gcd(b, a % b)

print(gcd(48, 18))  # 6
print(gcd(-48, 18))  # 6
print(gcd(17, 13))  # 1
print(gcd(0, 5))  # 5
print(gcd(0, 0))  # prints Error and returns none