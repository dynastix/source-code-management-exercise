def gcd(a: int, b: int) -> int:
    if a > b:
        minimum = b
    else:
        minimum = a
    for i in range(1, minimum + 1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
             
    return gcd

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
