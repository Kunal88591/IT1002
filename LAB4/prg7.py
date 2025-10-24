
# WAP: Check if two strings are anagrams

s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("Strings are Anagrams")
else:
    print("Strings are NOT Anagrams")
