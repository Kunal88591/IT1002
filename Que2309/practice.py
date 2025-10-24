
# -------------------------------
# 1. Square Pattern
# -------------------------------
"""
*****
*****
*****
*****
*****
"""
n = 5
for i in range(n):
    print("*" * n)


# -------------------------------
# 2. Right-Angled Triangle (increasing)
# -------------------------------
"""
*
**
***
****
*****
"""
n = 5
for i in range(1, n + 1):
    print("*" * i)


# -------------------------------
# 3. Inverted Right-Angled Triangle
# -------------------------------
"""
*****
****
***
**
*
"""
n = 5
for i in range(n, 0, -1):
    print("*" * i)


# -------------------------------
# 4. Right-Aligned Triangle
# -------------------------------
"""
    *
   **
  ***
 ****
*****
"""
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)


# -------------------------------
# 5. Inverted Right-Aligned Triangle
# -------------------------------
"""
*****
 ****
  ***
   **
    *
"""
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)


# -------------------------------
# 6. Pyramid
# -------------------------------
"""
    *
   ***
  *****
 *******
*********
"""
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# -------------------------------
# 7. Inverted Pyramid
# -------------------------------
"""
*********
 *******
  *****
   ***
    *
"""
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# -------------------------------
# 8. Diamond
# -------------------------------
"""
    *
   ***
  *****
   ***
    *
"""
n = 3
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# -------------------------------
# 9. Hollow Pyramid
# -------------------------------
"""
    *
   * *
  *   *
 *     *
*********
"""
n = 5
for i in range(1, n):
    if i == 1:
        print(" " * (n - i) + "*")
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
print("*" * (2 * n - 1))


# -------------------------------
# 10. Hollow Diamond
# -------------------------------
"""
   *
  * *
 *   *
  * *
   *
"""
n = 3
for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - i) + "*")
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
for i in range(n - 1, 0, -1):
    if i == 1:
        print(" " * (n - i) + "*")
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")


# -------------------------------
# 11. Hourglass
# -------------------------------
"""
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
"""
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# -------------------------------
# 12. Butterfly
# -------------------------------
"""
*      *
**    **
***  ***
********
***  ***
**    **
*      *
"""
n = 4
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)


# -------------------------------
# 13. Floyd’s Triangle
# -------------------------------
"""
1
2 3
4 5 6
7 8 9 10
"""
n = 4
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# -------------------------------
# 14. Continuous Numbers
# -------------------------------
"""
1
12
123
1234
"""
n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# -------------------------------
# 15. Repeated Numbers
# -------------------------------
"""
1
22
333
4444
"""
n = 4
for i in range(1, n + 1):
    print(str(i) * i)


# -------------------------------
# 16. Palindromic Number Pyramid
# -------------------------------
"""
   1
  212
 32123
4321234
"""
n = 4
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i + 1):
        print(j, end="")
    print()


# -------------------------------
# 17. Pascal’s Triangle
# -------------------------------
"""
1
1 1
1 2 1
1 3 3 1
"""
n = 4
for i in range(n):
    c = 1
    for j in range(i + 1):
        print(c, end=" ")
        c = c * (i - j) // (j + 1)
    print()


# -------------------------------
# 18. Binary Pattern
# -------------------------------
"""
1
0 1
1 0 1
0 1 0 1
"""
n = 4
for i in range(1, n + 1):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()


# -------------------------------
# 19. Alphabet Triangle
# -------------------------------
"""
A
AB
ABC
ABCD
"""
n = 4
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()


# -------------------------------
# 20. Alphabet Pyramid
# -------------------------------
"""
   A
  ABA
 ABCBA
ABCDCBA
"""
n = 4
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i, 0, -1):
        print(chr(64 + j), end="")
    for j in range(2, i + 1):
        print(chr(64 + j), end="")
    print()


# -------------------------------
# 21. Hollow Square
# -------------------------------
"""
*****
*   *
*   *
*   *
*****
"""
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")


# -------------------------------
# 22. X Pattern
# -------------------------------
"""
*   *
 * *
  *
 * *
*   *
"""
n = 5
for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# -------------------------------
# 23. Plus Pattern
# -------------------------------
"""
  *
  *
*****
  *
  *
"""
n = 5
for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# -------------------------------
# 24. Checkerboard
# -------------------------------
"""
* * * * *
 * * * * 
* * * * *
 * * * * 
* * * * *
"""
n = 5
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# -------------------------------
# 25. Spiral Matrix (3x3)
# -------------------------------
"""
1 2 3
8 9 4
7 6 5
"""
n = 3
a = [[0] * n for _ in range(n)]
num = 1
top, left = 0, 0
bottom, right = n - 1, n - 1
while top <= bottom and left <= right:
    for j in range(left, right + 1):
        a[top][j] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        a[i][right] = num
        num += 1
    right -= 1
    for j in range(right, left - 1, -1):
        a[bottom][j] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        a[i][left] = num
        num += 1
    left += 1
for r in a:
    print(*r)


# -------------------------------
# 26. Heart Shape
# -------------------------------
"""
 **   **
**** ****
*********
 ********
  ******
   ****
    **
     *
"""
n = 6
for i in range(n // 2, n, 2):
    print(" " * (n - i - 1) + "*" * i + " " * (n - i) + "*" * i)
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# -------------------------------
# 27. Christmas Tree
# -------------------------------
"""
   *
  ***
 *****
   *
  ***
 *****
   *
  ***
 *****
   *
   *
"""
n = 3
for k in range(3):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n):
    print(" " * (n - 1) + "*")
