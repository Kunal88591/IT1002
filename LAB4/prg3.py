# WAP to  Check if a string is palindrome

s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
