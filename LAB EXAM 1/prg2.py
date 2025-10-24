# Q2: Multiply only integer values in a dictionary by a given number , for the other type of values keep it same 

data = {"a": 151,"b": "kunal","c": 65,"d": 3.5,"e": "meena"}

factor = int(input("Enter value which you wanna multiply by an integer values "))

for key, value in data.items():
    if isinstance(value, int) and not isinstance(value, str):  
        data[key] = value * factor

print("Updated dictionary:", data)