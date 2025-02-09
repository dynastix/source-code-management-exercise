def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if a < 0 or b < 0:
        print("wrong input")
        return 
    
    # make sure 'a' is always the bigger number
    a, b = max(a,b), min(a,b)
    
    # check for remainder (b) equals '0'
    if b == 0:
        return a # return GCD
    else:
       return gcd(b, a % b) # recursivelly find the GCD



# Test cases:
# GCD(252,105) = 21 
# GCD(48,18) = 6 
# GCD(1445,1190) = 85 

a = [252, 48, 1445] 
b = [105, 18, 1190]

for i in range(3):
    ans = gcd(a[i], b[i])
    print(f"GCD({a[i]},{b[i]}) = {ans} ")