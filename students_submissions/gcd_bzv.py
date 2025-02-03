def gcd(a: int, b: int) -> int:

    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm with recursion.
    """

    if not isinstance(a, int) or not isinstance(b, int):
        # print("type error")
        return None;

    if a < 0 or b < 0:
        # print("Positive numbers only!");
        return None;

    if a == 0 and b == 0:
        # print("GCD(0,0) is not defined!");
        return None;
    # Base Case
    if b == 0:
        return a;
    # Recursive Step
    return gcd(b, a % b);

# Test Cases
print(gcd(54, 24));   # Expected: 6
print(gcd(48, 18));   # Expected: 6
print(gcd(101, 10));  # Expected: 1
print(gcd(0, 5));     # Expected: 5
print(gcd(7, 0));     # Expected: 7
print(gcd(1, 1));     # Expected: 1
print(gcd(1, 999));   # Expected: 1
print(gcd(0, 0));     # Error
print(gcd(-5, 10));   # Error
print(gcd(20, -4));   # Error
print(gcd(-8, -12));  # Error
print(gcd("2", 4));   # Error
