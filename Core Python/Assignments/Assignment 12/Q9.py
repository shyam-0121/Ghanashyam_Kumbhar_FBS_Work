# Calculate the number of words and the number of characters in a string
def number_of_words_and_characters(Str):
    words = 0
    chars = 0

    for i in Str:
        chars += 1
        if i == ' ':
            words += 1

    words += 1
    return words, chars

string = input('Enter Character/Word : ')
w , c = number_of_words_and_characters(string)
print('Words : ', w)
print('Characters : ', c)