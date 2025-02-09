def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """

    # Implement your solution here
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error, integers please")
        return None
    
    if a == 0 and b == 0:
        print("Error, undefined")
        return None

    while b != 0:
        a, b = b, a % b
    return abs(a)

    #pass
