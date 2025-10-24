#check wheather its print number or not 

num = int(input("Enter number"))
if(num >1):
    for i in range(2,num):
        if(num%i)==0:
            print(num ,"isnt a prime number")
            break

    else:
        print(num ,"is a prime number")
else:
    print("enter valid number")

