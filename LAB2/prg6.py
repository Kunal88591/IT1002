# print fibonacci series for n terms  

n =(int(input("Enter number")))
a, b = 0, 1
series = []
for i in range(n):
    series.append(a)
    a, b = b, a + b
print(series)


  

