# Question 3: Set-Based String Overlap Analysis
# Given two sets of strings, find all pairs of strings (one from 
# each set) that share at least one common substring of length 3 
# or more (case-sensitive). For each pair, return the longest 
# common substring. 
# Example: set1={"hello","world"}, set2={"hell","below"} 
# → { (("hello","hell"),"hell"), (("hello","below"),"low") }



set1 = {"hello", "world"}
set2 = {"hell", "below"}

result = set()

for s1 in set1:
    for s2 in set2:
        longest = ""
        for i in range(len(s1)):
            for j in range(i+1, len(s1)+1):
                sub = s1[i:j]
                if len(sub) >= 3 and sub in s2 and len(sub) > len(longest):
                    longest = sub
        if longest != "":
            result.add(((s1, s2), longest))

print(result)
