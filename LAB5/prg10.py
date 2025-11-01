# 10. WAP to append data to a file, and handle exceptions if the file is read-only.
try:
    f = open("data.txt", "a")   # append mode
    f.write("New line added\n")
    f.close()
    print("Data appended successfully")
except PermissionError:
    print("File is read-only, cannot write")
