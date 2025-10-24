# Question 4: Tuple-Based Dictionary Merging
# Given two dictionaries with tuple keys (each tuple contains two integers) 
# and integer values, merge them into a single dictionary. 
# If two keys are identical, their values should be added. 
# If a key from one dictionary has a "neighbor" key in the other dictionary 
# (where a neighbor key is one where both integers differ by at most 1), 
# multiply their values instead of adding them.



d1 = {(1, 1): 2, (2, 2): 3}
d2 = {(1, 2): 4, (3, 3): 5}

merged = {}

for k, v in d1.items():
    if k in d2:
        merged[k] = v + d2[k]
    else:
        found = False
        for k2, v2 in d2.items():
            if abs(k[0] - k2[0]) <= 1 and abs(k[1] - k2[1]) <= 1:
                merged[k] = v * v2
                found = True
                break
        if not found:
            merged[k] = v

for k, v in d2.items():
    if k not in merged:
        merged[k] = v

print(merged)
