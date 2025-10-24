#WAP TO FIND LARGEST OF THREE NUMBERS 

num1 = int(input("ENTER THE NUMBER1 :"))
num2 = int(input("ENTER THE NUMBER2 :"))
num3 = int(input("ENTER THE NUMBER3 :"))

if (num1 >num2):
    if(num1>num3):
        print("largest number is",num1)
    else:
        print("largest number is",num3)
else:
    if(num2>num3):
        print("largest number is",num2)
    else:
        print("largest number is",num3)

