# WAP: Count vowels and digits in a string

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
digit_count = 0

for ch in s:
    if ch in vowels:
        vowel_count += 1
    elif ch.isdigit():
        digit_count += 1

print(f"Vowels: {vowel_count}")
print(f"Digits: {digit_count}")
