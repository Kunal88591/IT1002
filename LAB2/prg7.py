num =int(input("Enter number:"))
factorial =1

if(num <0):
    print("factorial doesnt exist for ")
for i in range(1 , num+1):
    factorial*=i
print(factorial)

