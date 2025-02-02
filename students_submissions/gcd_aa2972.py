def gcd(a:int, b:int) -> int:

    if type(a) is not int or type(b) is not int:
        print("Error: wrong input (must be int)")
        return None
    
    if b == 0:
        return abs(a)
    return gcd(b, a%b)

#test cases
print(gcd(49, 28))
print(gcd(6, 0)) #zero as an input
print(gcd(28, 28)) #identical numbers
print(gcd(-34, -20)) #negative numbers
print(gcd(41, 23)) #prime numbers
print(gcd(200000000, 500000000)) #large numbers
print(gcd(6, "wrong"))
print(gcd("wrong", 0))
