# ==========================
# 50 Sample Python Questions
# ==========================

# Q1: Fibonacci
print("Q1:")
a, b = 0, 1
while a < 20:
    print(a, end=" ")
    a, b = b, a+b
print("\nConcept: Fibonacci using tuple swap")
print("Output: 0 1 1 2 3 5 8 13")
print("------\n")

# Q2: Default Argument
print("Q2:")
x = 10
def f(arg=x):
    print(arg)
x = 20
f()
print("Concept: Default evaluated at definition")
print("Output: 10")
print("------\n")

# Q3: For-Else Prime
print("Q3:")
for n in range(2, 8):
    for x in range(2, n):
        if n % x == 0:
            print(n, "=", x, "*", n//x)
            break
    else:
        print(n, "is prime")
print("Concept: for-else executes when loop not broken")
print("------\n")

# Q4
print("Q4:", list(range(20, -10, -5)))
print("Concept: Negative step in range")
print("Output: [20, 15, 10, 5, 0, -5]")
print("------\n")

# Q5
print("Q5:")
words = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(words)):
    print(i, words[i])
print("Concept: Indexing list")
print("------\n")

# Q6
print("Q6:", 2*"py" + "thon")
print("Concept: String multiplication")
print("Output: pypython")
print("------\n")

# Q7
a = [1, 2]; b = ["x","y"]; c = [a,b]
print("Q7:", c)
print("Concept: Nested lists")
print("Output: [[1, 2], ['x', 'y']]")
print("------\n")

# Q8
print("Q8:", range(5))
print("Concept: range object in Python3")
print("Output: range(0, 5)")
print("------\n")

# Q9
def f(a, L=[]):
    L.append(a); return L
print("Q9:")
print(f(1)); print(f(2)); print(f(3))
print("Concept: Mutable default persists across calls")
print("Output: [1], [1, 2], [1, 2, 3]")
print("------\n")

# Q10
def f(a, L=None):
    if L is None: L=[]
    L.append(a); return L
print("Q10:")
print(f(1)); print(f(2)); print(f(3))
print("Concept: Safe default using None")
print("Output: [1], [2], [3]")
print("------\n")

# Q11
print("Q11:", "python"[1:4])
print("Concept: String slicing")
print("Output: yth")
print("------\n")

# Q12
print("Q12:", "hello"[::-1])
print("Concept: Reverse string with slicing")
print("Output: olleh")
print("------\n")

# Q13
print("Q13:", [0,1,2,3,4,5][::2])
print("Concept: List slicing with step")
print("Output: [0,2,4]")
print("------\n")

# Q14
print("Q14:", [1,2]+[3,4])
print("Concept: List concatenation")
print("Output: [1,2,3,4]")
print("------\n")

# Q15
print("Q15:", [1,2]*3)
print("Concept: List repetition")
print("Output: [1,2,1,2,1,2]")
print("------\n")

# Q16
print("Q16:", "a" in "cat")
print("Concept: Membership operator")
print("Output: True")
print("------\n")

# Q17
print("Q17:", list({"a":1,"b":2}.keys()))
print("Concept: Dictionary keys")
print("Output: ['a','b']")
print("------\n")

# Q18
print("Q18:", {}.get("x",10))
print("Concept: dict.get with default")
print("Output: 10")
print("------\n")

# Q19
print("Q19:", {1,2,3,2})
print("Concept: Sets remove duplicates")
print("Output: {1,2,3}")
print("------\n")

# Q20
print("Q20:", {1,2,3}&{3,4,5}, {1,2,3}|{3,4,5})
print("Concept: Set operations AND/OR")
print("Output: {3} {1,2,3,4,5}")
print("------\n")

# Q21
print("Q21:", (1,2,3)[1])
print("Concept: Tuple indexing")
print("Output: 2")
print("------\n")

# Q22
print("Q22:", True+True+False)
print("Concept: Booleans act like 1/0")
print("Output: 2")
print("------\n")

# Q23
print("Q23:", int("123")+5)
print("Concept: Type casting")
print("Output: 128")
print("------\n")

# Q24
print("Q24:", 7/2)
print("Concept: Float division")
print("Output: 3.5")
print("------\n")

# Q25
print("Q25:", 7//2)
print("Concept: Floor division")
print("Output: 3")
print("------\n")

# Q26
print("Q26:", 7%2)
print("Concept: Modulus operator")
print("Output: 1")
print("------\n")

# Q27
print("Q27:", 2**3)
print("Concept: Power operator")
print("Output: 8")
print("------\n")

# Q28
print("Q28:", "-".join(["a","b","c"]))
print("Concept: String join")
print("Output: a-b-c")
print("------\n")

# Q29
print("Q29:", "a,b,c".split(","))
print("Concept: String split")         
print("------\n")

# Q30
print("Q30:", "hello".upper())
print("Concept: String upper()")
print("Output: HELLO")
print("------\n")

# Q31
print("Q31:", min([4,2,9]), max([4,2,9]))
print("Concept: Min/Max")
print("Output: 2 9")
print("------\n")

# Q32
print("Q32:", sum([1,2,3]))
print("Concept: Sum of list")
print("Output: 6")
print("------\n")

# Q33
print("Q33:", sorted([3,1,2]))
print("Concept: Sorted list")
print("Output: [1,2,3]")
print("------\n")

# Q34
print("Q34:", [x*x for x in range(5)])
print("Concept: List comprehension")
print("Output: [0,1,4,9,16]")
print("------\n")

# Q35
print("Q35:", [x for x in range(10) if x%2==0])
print("Concept: Filter even numbers")
print("Output: [0,2,4,6,8]")
print("------\n")

# Q36
print("Q36:", list(zip([1,2],["x","y"])))
print("Concept: Zip two lists")
print("Output: [(1,'x'),(2,'y')]")
print("------\n")

# Q37
print("Q37:")
for i,val in enumerate(["a","b"]):
    print(i,val)
print("Concept: Enumerate gives index and value")
print("Output: 0 a ; 1 b")
print("------\n")

# Q38
print("Q38:", any([0,1,0]), all([1,1,0]))
print("Concept: any vs all")
print("Output: True False")
print("------\n")

# Q39
print("Q39:", list(reversed([1,2,3])))
print("Concept: reversed()")
print("Output: [3,2,1]")
print("------\n")

# Q40
print("Q40:", list(map(str,[1,2,3])))
print("Concept: map function")
print("Output: ['1','2','3']")
print("------\n")

# Q41
f = lambda x:x+1
print("Q41:", f(5))            #A lambda function in Python is a small, anonymous function (doesn’t need a def name).
print("Concept: Lambda function")     #It returns the result of the expression when called.
print("Output: 6")
print("------\n")

# Q42
x=5
def f(): 
    x=10; print(x)
f(); print(x)
print("Q42 Concept: Local vs Global scope")
print("Output: 10 then 5")
print("------\n")

# Q43
x=5
def f():
    global x
    x=10
f()
print("Q43:", x)
print("Concept: global keyword")
print("Output: 10")
print("------\n")

# Q44
a=[1,2,3]; b=a; b.append(4)
print("Q44:", a)
print("Concept: Aliasing")
print("Output: [1,2,3,4]")
print("------\n")

# Q45
a=[1,2,3]; b=a[:]; b.append(4)
print("Q45:", a,b)
print("Concept: Shallow copy")
print("Output: [1,2,3] [1,2,3,4]")
print("------\n")

# Q46
a=[1,2]; b=[1,2]
print("Q46:", a==b, a is b)
print("Concept: Equality vs Identity")
print("Output: True False")
print("------\n")

# Q47
a="hello"; b="hello"
print("Q47:", a is b, a==b)
print("Concept: String interning")
print("Output: True")
print("------\n")

# Q48
print("Q48:", 0 or 5, 0 and 5)
print("Concept: Boolean operators short-circuit")
print("Output: 5 0")
print("------\n")

# Q49
def f(): print("called"); return True
print("Q49:", False and f())
print("Concept: Short circuit stops evaluation")
print("Output: False (function not called)")
print("------\n")

# Q50
try:
    1/0
except ZeroDivisionError:
    print("errror bhaisab ")
print("Concept: Exception handling")
print("Output: Error!")
print("------\n")
