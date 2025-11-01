# 2. WAP to count the number of lines and number of characters in your file named python.txt.

f = open("python_written.txt", "r")
lines = f.readlines()

line_count = len(lines)
char_count = 0

for line in lines:
    char_count += len(line)    

print("Lines:", line_count)
print("Characters:", char_count)

f.close()
