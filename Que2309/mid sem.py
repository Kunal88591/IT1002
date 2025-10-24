# Mid-Semester Exam Solutions
# Course: Introduction to Programming using Python (ECE)

print("Q1:")
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b
# Output: 0 1 1 2 3 5 8
print("------\n")

print("Q2:")
i = 5
def f(arg=i):
    print(arg)
i = 6
f()
# Output: 5
print("------\n")

print("Q3:")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        print(n, 'is a prime number')
# Output:
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3
print("------\n")

print("Q4:")
print(list(range(10, -100, -30)))
# Output: [10, -20, -50, -80]
print("------\n")

print("Q5:")
a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])
# Output:
# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb
print("------\n")

print("Q6:")
print(3 * 'un' + 'ium')
# Output: unununium
print("------\n")

print("Q7:")
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
# Output: [['a', 'b', 'c'], [1, 2, 3]]
print("------\n")

print("Q8:")
print(range(10))
# Output: range(0, 10)
print("------\n")

print("Q9:")
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
# Output:
# [1]
# [1, 2]
# [1, 2, 3]
print("------\n")

print("Q10:")
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
# Output:
# [1]
# [2]
# [3]
print("------\n")






