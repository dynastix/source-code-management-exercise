#Datha Bindumalam db624
#CS490-102 Exercise 2 
#01/28/25

#This function calculates the greatest common divisor of two integers
#The GCD is calculated using Euclid's algorithm
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    elif a > b:
        return gcd(b, a%b)
    else:
        return gcd(a, b%a)
