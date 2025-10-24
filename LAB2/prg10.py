# WAP to count number of vowels in a string

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print(f"Number of vowels in '{text}' is: {count}")
