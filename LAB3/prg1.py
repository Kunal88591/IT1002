# Find second largest number in list

numbers = [10, 20, 4, 45, 99, 99]

unique_nums = list(set(numbers))  
unique_nums.sort()

if len(unique_nums) >= 2:
    print("Second Largest:", unique_nums[-2])
else:
    print("List don't have 2 unique elements")
