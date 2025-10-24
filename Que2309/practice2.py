# =========================
# 1. BASICS & I/O
# =========================

# Swap two numbers without third variable
a, b = 5, 10
a, b = b, a
print("Swapped:", a, b)

# Celsius <-> Fahrenheit
c = 37
f = (c * 9/5) + 32
print("C to F:", f)
print("F to C:", (f - 32) * 5/9)

# Area & Circumference of circle
r = 5
print("Area:", 3.14*r*r, "Circum:", 2*3.14*r)

# Even or Odd
n = 7
print("Even" if n%2==0 else "Odd")

# Largest of 3 numbers
a,b,c = 10,20,15
print("Largest:", max(a,b,c))

# ASCII value
ch = 'A'
print("ASCII:", ord(ch))

# Reverse a number
num = 1234
rev = 0
temp = num
while temp>0:
    rev = rev*10 + temp%10
    temp//=10
print("Reverse:", rev)

# Sum of digits
num=1234
s=0
temp=num
while temp>0:
    s+=temp%10
    temp//=10
print("Digit sum:", s)


# =========================
# 2. CONDITIONALS
# =========================

# Leap year
year=2024
print("Leap" if (year%400==0 or (year%4==0 and year%100!=0)) else "Not Leap")

# Prime check
n=17
prime=True
if n<2: prime=False
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0: prime=False; break
print("Prime" if prime else "Not Prime")

# Armstrong number
n=153
s=0
temp=n
while temp>0:
    d=temp%10
    s+=d**3
    temp//=10
print("Armstrong" if s==n else "Not")

# Palindrome number
n=121
temp=n; rev=0
while temp>0:
    rev=rev*10+temp%10
    temp//=10
print("Palindrome" if rev==n else "Not")

# Grade based on marks
marks=85
if marks>=90: grade="A"
elif marks>=75: grade="B"
elif marks>=50: grade="C"
else: grade="F"
print("Grade:", grade)

# Quadratic roots
a,b,c=1,-3,2
d=b*b-4*a*c
if d>=0:
    r1=(-b+d**0.5)/(2*a)
    r2=(-b-d**0.5)/(2*a)
    print("Roots:", r1,r2)
else:
    print("Imaginary roots")


# =========================
# 3. LOOPS & SERIES
# =========================

# Fibonacci up to n
n=7
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
print()

# Factorial
n=5; fact=1
for i in range(1,n+1): fact*=i
print("Factorial:", fact)

# GCD & LCM
a,b=12,18
x,y=a,b
while b: a,b=b,a%b
gcd=a
lcm=(x*y)//gcd
print("GCD:", gcd, "LCM:", lcm)

# Multiplication table
n=5
for i in range(1,11): print(n,"x",i,"=",n*i)

# Sum of natural numbers
n=10
print("Sum:", n*(n+1)//2)

# Count digits
n=12345
print("Digits:", len(str(n)))

# Reverse string using loop
s="hello"; rev=""
for ch in s: rev=ch+rev
print("Reverse string:", rev)


# =========================
# 4. PATTERNS
# =========================

# Right-angled triangle
for i in range(1,6): print("*"*i)

# Pyramid
for i in range(1,6): print(" "*(5-i)+"*"*(2*i-1))

# Inverted pyramid
for i in range(5,0,-1): print(" "*(5-i)+"*"*(2*i-1))

# Floyd’s triangle
num=1
for i in range(1,6):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()

# Pascal’s triangle
n=5
for i in range(n):
    print(" "*(n-i),end="")
    val=1
    for j in range(i+1):
        print(val,end=" ")
        val=val*(i-j)//(j+1)
    print()

# Diamond
n=5
for i in range(1,n+1): print(" "*(n-i)+"*"*(2*i-1))
for i in range(n-1,0,-1): print(" "*(n-i)+"*"*(2*i-1))

# Number triangle
for i in range(1,6):
    for j in range(1,i+1): print(j,end="")
    print()

# Character triangle
for i in range(1,6):
    for j in range(65,65+i): print(chr(j),end="")
    print()


# =========================
# 5. STRINGS
# =========================

s="Hello123@#"
v=c=d=sp=0
for ch in s:
    if ch.lower() in "aeiou": v+=1
    elif ch.isalpha(): c+=1
    elif ch.isdigit(): d+=1
    else: sp+=1
print("Vowels:",v,"Consonants:",c,"Digits:",d,"Special:",sp)

# Reverse string without slicing
s="python"; rev=""
for ch in s: rev=ch+rev
print("Reverse:",rev)

# Anagram
s1,s2="listen","silent"
print("Anagram" if sorted(s1)==sorted(s2) else "Not")

# Frequency of characters
s="banana"; freq={}
for ch in s: freq[ch]=freq.get(ch,0)+1
print("Frequency:",freq)

# Substring search
s="hello world"; sub="world"
print("Found" if sub in s else "Not found")

# Remove vowels
s="beautiful"
out=""
for ch in s:
    if ch.lower() not in "aeiou": out+=ch
print(out)

# Upper/lowercase without inbuilt
s="AbC"
up=""; low=""
for ch in s:
    if 'a'<=ch<='z': up+=chr(ord(ch)-32); low+=ch
    elif 'A'<=ch<='Z': low+=chr(ord(ch)+32); up+=ch
    else: up+=ch; low+=ch
print("Upper:",up,"Lower:",low)


# =========================
# 6. LISTS
# =========================

lst=[3,1,4,1,5,9]

print("Max:",max(lst),"Min:",min(lst))

# Reverse list
rev=[]
for i in range(len(lst)-1,-1,-1): rev.append(lst[i])
print("Reversed:",rev)

# Sort manually
arr=[5,2,9,1]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print("Sorted:",arr)

# Merge lists
a=[1,2]; b=[3,4]; print("Merged:",a+b)

# Frequency of list elements
freq={}
for x in lst: freq[x]=freq.get(x,0)+1
print("Freq:",freq)

# Remove duplicates
unique=[]
for x in lst:
    if x not in unique: unique.append(x)
print("No duplicates:",unique)

# Second largest
arr=[10,20,5,8,15]
first=second=-9999
for x in arr:
    if x>first: second=first; first=x
    elif x>second and x!=first: second=x
print("Second largest:",second)


# =========================
# 7. TUPLES & SETS
# =========================

tup=(5,12,7,20,3)
print("Max:",max(tup),"Min:",min(tup))

# List <-> Tuple
lst=[1,2,3]
tup=tuple(lst)
lst2=list(tup)
print(tup,lst2)

# Set operations
a={1,2,3}; b={2,3,4}
print("Union:",a|b,"Intersection:",a&b,"Diff:",a-b)

# Remove duplicates using set
lst=[1,2,2,3,3]
print(list(set(lst)))


# =========================
# 8. DICTIONARIES
# =========================

# Word freq in string
s="this is a test this is"
words=s.split()
freq={}
for w in words: freq[w]=freq.get(w,0)+1
print("Word freq:",freq)

# Merge dictionaries
d1={"a":1,"b":2}; d2={"b":3,"c":4}
d1.update(d2)
print(d1)

# Sort by keys
d={"c":3,"a":1,"b":2}
print("By keys:",dict(sorted(d.items())))
print("By values:",dict(sorted(d.items(),key=lambda x:x[1])))

# Key with max value
d={"a":10,"b":25,"c":7}
print("Max key:",max(d,key=d.get))


# =========================
# EXTRA CONDITIONALS
# =========================

# Divisible by 3 & 5
n=15
if n%3==0 and n%5==0: print("Div by both")
elif n%3==0: print("Div by 3")
elif n%5==0: print("Div by 5")
else: print("Neither")

# Triangle type
a,b,c=3,3,3
if a==b==c: print("Equilateral")
elif a==b or b==c or a==c: print("Isosceles")
else: print("Scalene")

# 4-digit sum check
n=1233
s=str(n)
print("Equal" if int(s[0])+int(s[1])==int(s[2])+int(s[3]) else "Not")


# =========================
# EXTRA LOOPS
# =========================

# Primes 1-100
for n in range(2,101):
    for i in range(2,int(n**0.5)+1):
        if n%i==0: break
    else: print(n,end=" ")
print()

# Strong number (sum of factorial of digits)
n=145; s=0; temp=n
while temp>0:
    d=temp%10
    f=1
    for i in range(1,d+1): f*=i
    s+=f
    temp//=10
print("Strong" if s==n else "Not")

# Armstrong 100-1000
for n in range(100,1000):
    s=0; temp=n
    while temp>0:
        d=temp%10
        s+=d**3
        temp//=10
    if s==n: print(n,end=" ")
print()

# Reverse number palindrome
n=121; temp=n; rev=0
while temp>0:
    rev=rev*10+temp%10
    temp//=10
print("Palindrome" if rev==n else "Not")

# Factorial series
n=5; fact=1
for i in range(1,n+1):
    fact*=i
    print(fact,end=" ")
print()

# Largest digit
n=394857; largest=0
temp=n
while temp>0:
    d=temp%10
    if d>largest: largest=d
    temp//=10
print("Largest digit:",largest)


# =========================
# EXTRA STRINGS
# =========================

s="beautiful day"
vowels="aeiou"; count={}
for v in vowels: count[v]=s.lower().count(v)
print(count)

# Pangram check
s="The quick brown fox jumps over the lazy dog"
print("Pangram" if set("abcdefghijklmnopqrstuvwxyz")<=set(s.lower()) else "Not")

# Longest word
s="Python is very powerful"
words=s.split()
print("Longest:", max(words,key=len))

# Remove duplicates preserve order
s="programming"; out=""
for ch in s:
    if ch not in out: out+=ch
print(out)

# Rotations
s1,s2="abcde","deabc"
print("Rotation" if len(s1)==len(s2) and s2 in s1+s1 else "Not")

# Word frequency
s="this is a test this is a test"
words=s.split()
freq={}
for w in words: freq[w]=freq.get(w,0)+1
print(freq)


# =========================
# EXTRA LISTS
# =========================

lst=[4,2,8,6,1]

# Second largest and smallest
first=second=float("-inf")
smallest=second_small=float("inf")
for x in lst:
    if x>first: second=first; first=x
    elif x>second and x!=first: second=x
    if x<smallest: second_small=smallest; smallest=x
    elif x<second_small and x!=smallest: second_small=x
print("Second largest:",second,"Second smallest:",second_small)

# Rotate list k=2
k=2
lst=[1,2,3,4,5]
rot=lst[k:]+lst[:k]
print("Left rotate:",rot)

# Common elements without sets
a=[1,2,3,4]; b=[3,4,5]
common=[]
for x in a:
    if x in b and x not in common: common.append(x)
print(common)

# Pairs sum to given
lst=[1,2,3,4,5]; target=6
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==target: print(lst[i],lst[j])

# Remove duplicates without set
lst=[1,2,2,3,1]
unique=[]
for x in lst:
    if x not in unique: unique.append(x)
print(unique)

# Most frequent element
lst=[1,2,2,3,3,3,4]
freq={}
for x in lst: freq[x]=freq.get(x,0)+1
print("Most frequent:",max(freq,key=freq.get))


# =========================
# EXTRA TUPLES
# =========================

t=(5,1,9,3)
print("Index max:",t.index(max(t)),"Index min:",t.index(min(t)))

# Squares
t=(1,2,3)
sq=tuple(x*x for x in t)
print(sq)

# Merge remove duplicates
t1=(1,2,3); t2=(3,4,5)
print(tuple(set(t1+t2)))

# Flatten tuple of tuples
t=((1,2),(3,4),(5,6))
flat=()
for sub in t: flat+=sub
print(flat)


# =========================
# EXTRA SETS
# =========================

a={1,2,3}; b={3,4,5}
print("Common:",a&b,"Union:",a|b,"Diff:",a-b)

# Subset check
print(a<=b)

# Common in 3 sets
a={1,2,3}; b={2,3,4}; c={3,4,5}
print("Common count:",len(a&b&c))

# Unique chars
s="hello world"
print(set(s.replace(" ","")))

# Pairs with even sum
a={1,2}; b={3,4}
for i in a:
    for j in b:
        if (i+j)%2==0: print(i,j)


# =========================
# EXTRA DICTIONARIES
# =========================

# Char freq
s="banana"
freq={}
for ch in s: freq[ch]=freq.get(ch,0)+1
print(freq)

# Word freq paragraph
s="this is a test. this test is simple."
words=s.split()
freq={}
for w in words: freq[w]=freq.get(w,0)+1
print(freq)

# Dict from lists
keys=["a","b","c"]; vals=[1,2,3]
d={}
for i in range(len(keys)): d[keys[i]]=vals[i]
print(d)

# Merge + add values
d1={"a":2,"b":3}; d2={"a":5,"c":7}
for k,v in d2.items(): d1[k]=d1.get(k,0)+v
print(d1)

# Key(s) with max value
d={"a":10,"b":25,"c":25}
m=max(d.values())
print([k for k,v in d.items() if v==m])

# Topper
students={"A":85,"B":92,"C":92}
top=max(students.values())
print([k for k,v in students.items() if v==top])

# Invert dictionary
d={"a":1,"b":2}
inv={v:k for k,v in d.items()}
print(inv)

# Dict equality
d1={"a":1,"b":2}; d2={"b":2,"a":1}
print("Equal" if d1==d2 else "Not")
