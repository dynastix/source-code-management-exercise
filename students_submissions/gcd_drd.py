def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two positive integers using recursion.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None
    if a <= 0 or b <= 0:
        print("Error: Both inputs must be positive integers.")
        return None

    return a if b == 0 else gcd(b, a % b)


# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(270, 192))  # Expected output: 6
