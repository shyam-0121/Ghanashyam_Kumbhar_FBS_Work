# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

def split_words(Str):
    words = []
    current = ''


    for char in Str:
        if char != ' ':
            current += char
        else:
            words.append(current)
            current = ''

    words.append(current)
    return words

def count_frequency(words):
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

String = input('Enter String : ')
words = split_words(String)
res = count_frequency(words)
print(res)
