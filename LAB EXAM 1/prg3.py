# Q3: Count vowels in a string a e i o u , ignoring case and  return vowels and their count in a dictionary 

text = "My Name is KUNAL MEENA"

vowels = "aeiou"
count1 = {v: 0 for v in vowels}  

for char in text.lower():
    if char in vowels:
        count1[char] += 1

print("Vowel counts:", count1)