#WAP TO CHECK BALANCE IN ATM 

balance = 4080
#password = 3764


print("Welcome - Please Enter you password here")
password = int((input("Enter your password:")))

while(True):   
    if (password !=3764):
        print("Invalid password")
    break

if password ==3764:
    print("1 - check balance")
    print("2 - withdrwal amount")


option=int(input("enter options- 1/2"))


if(option ==1):
    print(balance)
elif(option ==2):
    withdrawl =int(input("Enter amount to withdraw"))
    if(withdrawl  >=balance):
        print("not sufficient balance")
    else:
        balance-=withdrawl
        print("withdrawl success" )







 

