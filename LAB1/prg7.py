# Q2. Check divisibility by both 3 and 5 using logical operators
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Number is divisible by both 3 and 5")
else:
    print("Number is not divisible by both 3 and 5")