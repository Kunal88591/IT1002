# wap Split list into even and odd numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even)
print("Odd numbers:", odd)
