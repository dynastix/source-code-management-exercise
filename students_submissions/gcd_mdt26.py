def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    if (a >= b):
        r = a%b
        if (r == 0):
            return b
        else:
            return gcd(b, r)
    else:
        r = b%a
        if (r == 0):
            return a
        else:
            return gcd(a, r)
#    pass
print('a = ', end='')
a = int(input())
print()

print('b = ', end='')
b = int(input())
print()

print('GCD = ', gcd(a, b))

