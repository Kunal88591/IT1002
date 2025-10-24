# Find max and min in tuple



tup = (5, 12, 7, 20, 3, 15)

max_val = tup[0]
min_val = tup[0]

for num in tup:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Tuple:", tup)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
