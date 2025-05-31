



import math

def gcd(a: int, b: int) -> int:

    # check if negative numbers:
    # 
    if(a < 0 or b < 0):

        print("Error: Cannot use negative numbers", a, ", ", b)
        return None


    # function checks for primes first:
    def primeCheck(num: int):
        # 1 is not prime
        if num <= 1:
            return False
        # 2 is prime
        if num == 2:
            return True
        # even numbers are not prime
        if num % 2 == 0:
            return False

        sqrt_n = int(math.sqrt(num))
        for i in range(3, sqrt_n + 1, 2):
            if num % i == 0:
                return False
        return True


    # check if a or b are primes, if so return 1 as that is the only common denominator between:
    #  unless they are equal prime, in which case return a or b:
    if(primeCheck(a)):
        # 2 is prime, but also equal, so.. gcd(10,2) is 2. so skip
        if(a!=2):
            if(a == b):
                return a
            if(b == 0):
                return a
            return 1
    # if A is prime and B is 0, A is returned;
    # if A is prime and B is the same value, A or B is returned;
    # if A is prime and B is some other value, such as a non-prime or another prime, then 1 is returned as gcd;
    # vice versa for B to the above;
    if(primeCheck(b)): 
        if(b!=2):
            if(a == b):
                return a
            if(a == 0):
                return b
            return 1

    # calculate the greatest common denominator:
    # 
    
    # recursively call the euclidean algorithm:
    # assuming we avoided the edge cases:
    
        # For values like A=10 and B = 0, the immediate return is A;
        # For Values A = 0 and B = 10, the next iteration will be gcd(B=10, and A%B == 0%10 == 0),
        #  which becomes gcd(10, 0), which is A==10 as well;
        #  
        # The algorithm, will mod the smaller into the larger;
        # If that value is 0, that is the gcd. Otherwise, the remainder is then put back into
        # The function with the previous B value, and they are again checked.
        # 
        # But, in general:
        # Example:
        # -> gcd(54, 24) B==0 ? No -> gcd(24, 54%24==6) B==0?No -> gcd(6, 24%6==0) B==0? Yes, return A==6 as gcd;
        # 

    if b == 0:
        return a
    else:
        return gcd(b, a % b)




# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 16
print(gcd(101, 10))  # Expected output: 1


# Edge Case Tests:
# primes, zeroes, etc
# print(gcd(101, 101))
# print(gcd(24, 54))

# print(gcd(0, 5))
# print(gcd(5, 0))

# print(gcd(0, 4))
# print(gcd(4, 0))


print(gcd(4, -5))
print(gcd(40, 2))
print(gcd(2, 12))


