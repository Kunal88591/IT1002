# 3. WAP to merge the content of two files.

f1 = open("python_written.txt", "r")
f2 = open("python_.txt", "r")
f3 = open("merged.txt", "w")

f3.write(f1.read())
f3.write("\n")   
f3.write(f2.read())

f1.close()
f2.close()
f3.close()

print("Files merged!")
