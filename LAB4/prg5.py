# WAP: Reverse words in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = " ".join(words[::-1])
print("Reversed Sentence:", reversed_sentence)
