# 4. WAP to display only the 3rd line of the text.

f = open("python_.txt", "r")
lines = f.readlines()

print("3rd line:",lines[2])   

f.close()
