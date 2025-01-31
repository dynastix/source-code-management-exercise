from sympy import isprime
def gcd(a: int, b: int) -> int:
	if a < 0 or b < 0:
		print("Negative detected")
		return
	if isprime(a) or isprime(b):
		print("Prime detected")
		return 1
	if b == 0:
		return a
	else:
		return gcd(b,a%b)

print(gcd(7, 13))
print(gcd(54, 24))
print(gcd(48, 18))
print(gcd(101, 10))
print(gcd(0, 0))