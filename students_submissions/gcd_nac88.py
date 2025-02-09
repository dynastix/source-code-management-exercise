#Nahallah Champagne

def gcd(a: int, b: int) -> int:
    
    if b == 0 or a == 0:
        print("Cant divide by zero. Try again.")
        return None

    #If a % b is 0, then return b, which holds the gcd
    if (a % b) == 0:
        if b < 0:
            return -b #turns num into positive, for neg inputs     
        return b
    else:
        #Modulus the number until its 0
        return gcd(b, a % b)
    

# Test cases
print(gcd(54, 24))  # Expected output: 6

    #(54, 24)
    #a % b = 6
    #gcd (24, 6)
    #a % b = 0
    #gcd (24, 0)

print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(20, 20))  #(Same number) Expected output: 20
print(gcd(36, 0))  # (Zero int)Expected output: None?
print(gcd(51, 7))  # (Prime numbers)Expected output: 1
print(gcd(8, -4))  # (Negative numbers)Expected output: (positve)4
print(gcd(10, 100)) #Expected output: 10
