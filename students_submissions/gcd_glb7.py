# Author: Giovani Bergamasco
# Date: 2/2/2025
# Course: CS 490
# Professor: William McCann
# Assignment: Exercise 2
# Description: Function to calculate the greatest common divisor of two integers using the euclidian method without using any loops aka using recursion.

def gcd(a: int, b: int) -> int:
    # Edge Case
    if a == 0 and b == 0:
        print("Undefined value for gcd(0, 0)")
        return None
    # Base Case
    if b == 0:
        return abs(a)
    # Recursive Case
    return gcd(b, a % b)

# Test Cases : expected results (5, 5, 5, 5, 5, 5, 5, 5, Undefined, 3)
print(gcd(10, 45)) # both positive (a<b)
print(gcd(45, 10)) # both postitive (a>b)
print(gcd(-10, 45)) # mixed sign (a<0, b>0)
print(gcd(10, -45)) # mixed sign (a>0, b<0)
print(gcd(-10, -45)) # both negative (a<b)
print(gcd(-45, -10)) # both negative (a>b)
print(gcd(5, 0)) # b is 0
print(gcd(0, 5)) # a is 0
print(gcd(0, 0))  # Undefined Case (a=0, b=0)
print(gcd(598740279859771020868226391647315179701125535902784618637527, 370370240865192802474151282959990087846199968994424134020533)) # large numbers

# Recursion depth case?
# There is nothing that can be done to prevent this case without using a loop.
# Python will automatically throw an error if the recursion depth is exceeded anyway.