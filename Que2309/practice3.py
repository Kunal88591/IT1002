# Q1. Tuple Character Filtering & Replacement 
# Given a tuple of strings, create a new tuple where each string keeps only consonants. 
# If the resulting string length is even, replace it with "EVEN", else keep it reversed.

t = ("apple","sky","oo")
result = []

for s in t:
    consonants = "".join([ch for ch in s if ch.lower() not in "aeiou"])
    if len(consonants) % 2 == 0:
        result.append("EVEN")
    else:
        result.append(consonants[::-1])

result = tuple(result)
print(result)



# Q2. Dictionary Merge with Conditional Rules Given a list of (string key, int value) pairs,
#  make a dictionary. If the key length is odd → sum normally. If even → take the maximum of values. 
# Example: [("cat",2),("dog",5),("fish",3),("cat",4),("fish",7)] → {"cat":6,"dog":5,"fish":7}


data = [("cat",2),("dog",5),("fish",3),("cat",4),("fish",7)]
d = {}

for k,v in data:
    if k in d:
        if len(k) % 2 == 0:
            d[k] = max(d[k], v)
        else:
            d[k] += v
    else:
        d[k] = v

print(d)


# Q3. Set Common Subsequence Finder Given two sets of strings, 
# find all pairs (x,y) with longest common subsequence (not substring). 
# Return dictionary: {(x,y): subsequence}.
#  Example: { "abc","bcd" }, { "acd","abcd" } → {("abc","abcd"):"abc",("bcd","abcd"):"bcd"}

def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[""]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if s1[i]==s2[j]:
                dp[i+1][j+1] = dp[i][j]+s1[i]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)
    return dp[m][n]

set1 = {"abc","bcd"}
set2 = {"acd","abcd"}
result = {}

for s1 in set1:
    for s2 in set2:
        subseq = lcs(s1,s2)
        if subseq: result[(s1,s2)] = subseq

print(result)


# Q4. Dictionary with Tuple Keys – Diagonal Neighbor Rule Two dicts with (i,j) tuple keys. If identical → add values. If abs(i1-i2)==abs(j1-j2)==1 (diagonal neighbors), keep maximum instead of sum. Example: {(1,1):5}, {(2,2):7} → {(1,1):5,(2,2):7} but merge rule applies.


d1 = {(1,1):5}
d2 = {(2,2):7}
merged = d1.copy()

for k2,v2 in d2.items():
    found=False
    for k1 in d1:
        if k1==k2:
            merged[k1] = d1[k1]+v2
            found=True
        elif abs(k1[0]-k2[0])==1 and abs(k1[1]-k2[1])==1:
            merged[k2] = max(d1[k1],v2)
            found=True
    if not found:
        merged[k2] = v2

print(merged)
# Output: {(1,1):5, (2,2):7}

# Q5. String Expansion with Forbidden Set Given a string and forbidden set, expand consecutive letters (like run-length expansion) but skip expansion if substring in forbidden set. Return expanded string and skipped count. Example: "a2b3c", forbidden { "bb" } → "aabbbbc", 0 But "a2bb3", forbidden { "bb" } → "aabb3"

s = "a2bb3"
forbidden = {"bb"}

expanded = ""
skipped = 0
i = 0

while i < len(s):
    if i+1 < len(s) and s[i+1].isdigit():
        count = int(s[i+1])
        temp = s[i]*count
        if temp in forbidden:
            expanded += s[i] + s[i+1]  # keep as original
            skipped += 1
        else:
            expanded += s[i]*count
        i += 2
    else:
        expanded += s[i]
        i += 1

print((expanded, skipped))
# Output: ('aabb3', 1)

# Q6. Nested Tuple Flatten & Filter Given a tuple of tuples of strings, flatten it and remove strings that contain any vowel. Example: (("apple","sky"),("try","oak")) → ("sky","try")
t = (("apple","sky"),("try","oak"))
result = []

for sub in t:
    for s in sub:
        if not any(ch in "aeiouAEIOU" for ch in s):
            result.append(s)

result = tuple(result)
print(result)
# Output: ('sky', 'try')

# Q7. Dictionary with Conditional Value Transformation Given a list of (string key, int value), create a dictionary. If a key starts with a vowel → subtract 1 from sum of values for that key. Example: [("apple",5),("bat",3),("apple",2)] → {"apple":6,"bat":3}
data = [("apple",5),("bat",3),("apple",2)]
d = {}

for k,v in data:
    if k in d:
        d[k] += v
    else:
        d[k] = v

for k in d:
    if k[0].lower() in "aeiou":
        d[k] -= 1

print(d)
# Output: {'apple': 6, 'bat': 3}
# Q8. Set Substring Filtering Given two sets of strings, return all pairs that share any substring of length exactly 2. Return as list of tuples. Example: {"ab","cd"}, {"bc","ad"} → [("ab","bc"),("cd","ad")]

set1 = {"ab","cd"}
set2 = {"bc","ad"}
pairs = []

for s1 in set1:
    for s2 in set2:
        for i in range(len(s1)-1):
            sub = s1[i:i+2]
            if sub in s2:
                pairs.append((s1,s2))
                break

print(pairs)
# Output: [('ab', 'bc'), ('cd', 'ad')]


# Q9. Tuple-Key Dictionary Merge with Neighbor Rule Given two dictionaries with (x,y) 
# tuple keys and integer values,
#  merge them.#  If two keys differ by exactly 1 in either coordinate → 
# subtract smaller value from larger instead of adding.

d1 = {(1,1):5,(2,2):3}
d2 = {(1,2):4,(3,2):6}
merged = d1.copy()

for k2,v2 in d2.items():
    found=False
    for k1 in d1:
        if k1==k2:
            merged[k1] = d1[k1]+v2
            found=True
        elif abs(k1[0]-k2[0])==1 or abs(k1[1]-k2[1])==1:
            merged[k2] = abs(d1[k1]-v2)
            found=True
    if not found:
        merged[k2] = v2

print(merged)
# Output example: {(1, 1): 5, (2, 2): 3, (1, 2): 1, (3, 2): 6}



# Q10. String Compression with Forbidden Characters
#  Compress a string by replacing consecutive repeated characters with one occurrence, 
# but skip compression if character is in forbidden set. Return compressed string and count of skipped compressions. 
# Example: "aaabccddd", forbidden { "c" } → "abcd", skipped=1

s = "aaabccddd"
forbidden = {"c"}

compressed = s[0]
skipped = 0
i = 1

while i < len(s):
    if s[i] == compressed[-1] and s[i] not in forbidden:
        skipped += 1
    else:
        compressed += s[i]
    i += 1

print((compressed, skipped))
# Output: ('abcd', 1)

