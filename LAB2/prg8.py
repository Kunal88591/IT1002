

# WAP to print number pyramid pattern

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    # Print spaces
    print(" " * (n - i), end="")
    
    # Print numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")
    
    print()  # Move to next line
