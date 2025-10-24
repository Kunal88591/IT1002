# WAP: GCD using Euclidean algorithm (function)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"GCD of {x} and {y} is {gcd(x, y)}")
