# Question 5: String Compression with Set Constraints
# Write a function that takes a string and a set of forbidden substrings. 
# Compress the string by replacing repeated consecutive substrings 
# with a single occurrence, but only if the substring is not in the forbidden set. 
# Return a tuple containing the compressed string and the number of replacements made. 
# Example: if input string is "aabaabaab" and forbidden set is {"aa"}, 
# result should be ("abaabab", 2).



s = "aabaabaab"
forbidden = {"aa"}

compressed = ""
i = 0
count = 0

while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]:
        j += 1
    segment = s[i:j]
    if len(segment) > 1 and segment not in forbidden:
        compressed += segment[0]
        count += 1
    else:
        compressed += segment
    i = j

print((compressed, count))
