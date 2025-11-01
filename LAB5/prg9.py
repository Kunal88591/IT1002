# 9 .WAP that tries to open data.txt; if it doesn't exist display "File not found" and create the file automatically if it is missing.

try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File not found, creating file...")
    f = open("data.txt", "w")
    f.write("File created automatically\n")
    f.close()
