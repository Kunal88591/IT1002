
# Question 1: Tuple Transformation with String Constraints
# Given a tuple of strings, create a new tuple where each string 
# is transformed such that all vowels are removed, and the 
# resulting string is reversed. If the transformed string is 
# empty, include "no_vowels" in the tuple instead. 
# Example: ("hello","world","aeiou") → ("lleh","dlrw","no_vowels")





data = ("hello", "world", "aeiou")

vowels = "aeiouAEIOU"
result = []

for s in data:
    new_s = ""
    for ch in s:
        if ch not in vowels:
            new_s += ch
    new_s = new_s[::-1]   
    if new_s == "":
        result.append("no_vowels")
    else:
        result.append(new_s)

result = tuple(result)
print(result)
