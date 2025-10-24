# WAP for Student database using dictionary

students = {} 

n = int(input("Enter number of students: "))
for i in range(n):
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students[roll] = {"Name": name, "Marks": marks}

print("Student Data")
for roll, info in students.items():
    print(f"Roll: {roll}, Name: {info['Name']}, Marks: {info['Marks']}")
