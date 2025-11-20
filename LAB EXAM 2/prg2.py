# 2 read a file and print only those lines that contain atleast 3 vowels 


def count_vow(s, i=0, c=0):

    if i == len(s):
        return c
        
    if s[i].lower() in "aeiou":
        c += 1
    return count_vow(s, i + 1, c)

with open("input.txt") as f:
    for line in f:
        if count_vow(line)>= 3:
            print(line, end="")
