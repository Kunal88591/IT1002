# Question 2: Dictionary Key Collision Resolution
# You have a list of tuples (string key, integer value). 
# Create a dictionary where keys are the strings and values are 
# the sum of all integers associated with that key. However, 
# if a key contains the substring "dup" (case-insensitive), its 
# final value should be doubled. 
# Example: [("key1",5),("dup_key",3),("key1",2),("DUP_test",4)] 
# → {"key1":7,"dup_key":6,"DUP_test":8}




data = [("key1", 5), ("dup_key", 3), ("key1", 2), ("DUP_test", 4)]

d = {}
for k, v in data:
    if k in d:
        d[k] += v
    else:
        d[k] = v


final = {}
for k in d:
    if "dup" in k.lower():
        final[k] = d[k] * 2
    else:
        final[k] = d[k]

print(final)
