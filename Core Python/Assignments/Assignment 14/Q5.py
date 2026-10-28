# Find the longest common prefix of all strings (use the Python set)

def long_comm_prefix(words):
    shortest = len(words[0])

    for w in words:
        count = 0
        for ch in w:
            count += 1
        if count < shortest:
            shortest = count

    prefix = ''
    for i in range(shortest):
        chars = set()
        for w in words:
            chars.add(w[i])

        if len(chars) == 1:
            prefix += words[0][i]
        else:
            break

    return prefix

words = ['flower', 'flow', 'flight']
res = long_comm_prefix(words)
print(res)
    





