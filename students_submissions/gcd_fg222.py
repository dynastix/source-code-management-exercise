def max (a: int, b: int) -> int:
    return a if a > b else b

def gcd (a: int, b: int) -> int:
    if b == 0:
        return max(a, -a)
    else:
        return gcd(b, a%b)

print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(54,-24))
print(gcd(-54,-24))
print(gcd(1071, -462))

