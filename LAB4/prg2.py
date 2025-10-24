# WAP: Count word frequency in a string

sentence = input("Enter a sentence: ")
words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

for w, c in freq.items():
    print(f"{w}: {c}")
