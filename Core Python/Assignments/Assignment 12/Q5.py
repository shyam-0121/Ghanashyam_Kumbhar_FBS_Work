# Python Program to Count the Number of Vowels in a String

def number_of_vowel(Str):
    vowel = 0

    for char in Str:
        if char.lower() in 'aeiou':
            vowel += 1

    return vowel

string = input('Enter String : ')
res = number_of_vowel(string)
print(res)