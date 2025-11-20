# 4 using recursion only compute the sum of digits of all numbers from 1 to n without using using loop and built in fn 

def sum_digits(x):
    if x == 0:
        return 0
    return x % 10 + sum_digits(x // 10)

def sum_all(n):
    if n == 0:
        return 0
    return sum_digits(n) + sum_all(n - 1)

n = int(input())
print(sum_all(n))
