s = "apple is a fruit , apple is in red colour"
words = s.split()
freq = {}

for word in words:
    word = word.strip(",.")
    freq[word] = freq.get(word, 0) + 1
    
for word, count in freq.items():
    if count > 1:
        print(f"'{word}' appears {count} times")
