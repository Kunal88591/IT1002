# WAP Check if element exists in tuple

tup = (13, 11, 20, 3, 27, 10 ,20 ,4)

element = int(input("Enter element to check :"))
if element in tup:
    print(f"{element} exists in tuple")
else:
    print(f"{element} does not exist in tuple")
