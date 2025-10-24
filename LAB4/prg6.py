# WAP: Caesar Cipher Encryption

text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value: "))
result = ""

for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        result += chr((ord(ch) - base + shift) % 26 + base)
    else:
        result += ch  

print("Encrypted text:", result)
