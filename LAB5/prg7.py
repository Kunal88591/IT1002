# 7. WAP to take age as input and raise a Value Error if the age is less than 18 (Age Validator).
age = int(input("Enter age: "))

try:
    if age < 18:
        raise ValueError("Age must be 18 or above")
    print("Valid age")
except ValueError as e:
    print(e)
