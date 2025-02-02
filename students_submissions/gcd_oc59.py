def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """

    #int check
    if not isinstance(a,int) or not isinstance(b,int):
        print("Error since inputs should be ints")
        return None

    #undefined case
    if a==0 and b==0:
        print("Error since gcd(0,0) is undefined")
        return None
    
    a,b= abs(a),abs(b)

    #helper
    def gcd_r(x,y):
        if y==0:
            return x
        return gcd_r(y, x%y)

    return gcd_r(a,b)


