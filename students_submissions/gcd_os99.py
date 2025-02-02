def gcd(a: int, b: int) -> int:

    try:

        if not (isinstance(a,int) and isinstance(b,int)):
            raise ValueError("both inputs have to be integers")

        a = int(a)
        b = int(b)

    except ValueError:

        print("invalid, both inputs must be integers")
        return None
    
    if a == 0 and b == 0:
        print("gcd of 0 and 0 is undefined")
        return None
    
    if b == 0:
        return abs(a)
    
    return gcd(b, a % b)


print (gcd(54,24))
print (gcd(48,18))
print (gcd(101,10))

    