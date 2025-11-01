#1. WAP to create a file and write 5 lines of text by taking it as input from the user.

f = open("python_.txt", "w")

for i in range(5):
    line = input("Enter line: ")
    f.write(line + "\n")

f.close()
print("Written successfully!")
