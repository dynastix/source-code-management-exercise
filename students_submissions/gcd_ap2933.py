def gcd(a: int, b: int) -> int:
    # check if int
    if not isinstance(a, int) or not isinstance(b, int):
        print("Input is not an integer")
        return None
    # check if integer
    if a < 0 or b < 0:
        print("Cannot enter negative numbers")
        return None
    # base case we can't divide anymore
    if b == 0:
        return a
    else:
        # recursive case, take a modulo b
        return gcd(b, a % b)

# Testing cases:
print(gcd("test", 24)) # expects None
print(gcd(-12, 28)) # expects None
print(gcd(12, -28)) # expects None
print(gcd(77, 10)) # expects 1
print(gcd(3, 7)) # expects 1
print(gcd(5, 20)) # expects 5
print(gcd(6, 36)) # expects 6
print(gcd(3, 99)) # expects 3
print(gcd(50, 5)) # expects 5
print(gcd(0, 2)) # expects 2
