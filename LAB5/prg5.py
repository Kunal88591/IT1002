# 5. WAP that opens a file, reads numbers line-by-line, and calculates their sum.

f = open("python_.txt", "r")
total = 0

for line in f:
    line = line.strip()
    if line.isdigit():
        total +=int(line)
    else:
        print("skipping invalid line",line)

    

print("Sum =", total)

f.close()
