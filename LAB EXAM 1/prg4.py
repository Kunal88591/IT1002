
# calculate grade based on marks such that 
# for marks 90+ give "A" and for marks 80-89 give "B" 
# and for marks 70-79 give "C" and for marks 60-69 give "D" and give F if less than 60
 
score = int(input("Enter score:"))


if score >100 or score <0:
    print("invalid input")
else :
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")


