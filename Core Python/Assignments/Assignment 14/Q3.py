# Find all the unique words and count their frequency from a given list of strings (use the set data type)

def count_freq(words):
    unique = set(words)

    for word in unique:
        count = 0
        for w in words:
            if w == word:
                count += 1
        print(word, ':', count)


words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
count_freq(words)
    
