def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Inputs must be integers.")
        return None
    if a == 0 and b == 0:
        print("Error: GCD is undefined for (0, 0).")
        return None
    if b == 0:
        return abs(a)
    return gcd(b, a % b)
