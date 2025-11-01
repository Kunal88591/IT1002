# 8. WAP that tries to open a file data.txt, if it doesn't exist display "File not found".
try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File not found")
