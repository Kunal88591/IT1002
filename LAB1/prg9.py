# Q4. Demonstrating logical operators with boolean values
a = bool(int(input("Enter first boolean (0 or 1): ")))
b = bool(int(input("Enter second boolean (0 or 1): ")))
c = bool(int(input("Enter third boolean (0 or 1): ")))

print("AND:", a and b and c)
print("OR:", a or b or c)
print("NOT a:", not a)
