
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
sorted_words = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)
print("Two most frequent words:")
for word, count in sorted_words[:2]:
    print(word, ":", count)
