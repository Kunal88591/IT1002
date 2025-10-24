# Count frequency of elements in list


numbers = [1, 2, 2, 3, 3, 3, 4, 5]

frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Frequency of elements:", frequency)
