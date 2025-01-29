def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    a = abs(a)
    b = abs(b)
    low = min(a,b)
    high = max(a,b)
    if low == 0:
        print("At least one of the numbers given is 0, so the gcd is the other number, if both are 0, then you will get 0")
        return high
    high = high % low
    if high == 0:
        if low == 1:
            print("At least one of the numbers given was a prime")
        return low
    return gcd(low,high)
    pass

print(gcd(123456, 7890))