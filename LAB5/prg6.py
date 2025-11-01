# 6. WAP to accept two numbers and divide them, but handle Zero Division Error.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    print("Result =", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
