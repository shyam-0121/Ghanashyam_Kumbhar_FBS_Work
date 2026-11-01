# Find all the anagrams and group them together from a given list of strings


def anagrams(words):
    groups = {}

    for word in words:
        key =''.join(sorted(word))

        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    for i in groups:
        print(groups[i])

words = ['listen', 'silent', 'enlist', 'google', 'gogole', 'cat', 'act']
anagrams(words)