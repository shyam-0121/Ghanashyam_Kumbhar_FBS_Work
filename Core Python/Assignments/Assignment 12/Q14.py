# Count the occurrences of each word in a string
# Count the occurrences of each word in a string

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


def count_words(words):
    counted = []

    for word in words:
        if word not in counted:
            count = 0
            for w in words:
                if w == word:
                    count += 1
            print(word, ':', count)
            counted.append(word)


String = input('Enter String : ')
words = split_words(String)
count_words(words)