# WAP to find GCD of two numbers (using loop)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b   # Euclidean algorithm

print("GCD is:", a)
