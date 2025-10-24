#WAP TO CHECK WHEATHER ITS LEAP YEAR OR NOT 

year =int(input("ENTER THE YEAR:"))

if ((year%4)==0 and (year%100)!=0):
    print("its a leap year")
else :
    print("not a leap year")
