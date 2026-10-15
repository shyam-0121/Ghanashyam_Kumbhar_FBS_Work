# Count the number of digits and letters in a string


def count_digits_strings(Str):
    digits = 0
    letters = 0

    for char in Str:
        if char >= '0' and char <= '9':
            digits += 1
        elif char.lower()  >= 'a' and char.lower() <= 'z':
            letters += 1

    return digits, letters

String = input('Enter String : ')
d, l = count_digits_strings(String)
print('Digits :', d)
print('Letters :', l)