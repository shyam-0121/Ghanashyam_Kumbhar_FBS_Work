# Python Program to Detect if Two Strings are Anagrams

def count_char(s, target):
    count = 0
    for ch in s:
        if ch == target:
            count += 1
    return count

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    for ch in str1:
        if count_char(str1, ch) != count_char(str2, ch):
            return False

    return True

str1 = input('Enter first string: ')
str2 = input('Enter second string: ')

res = is_anagram(str1, str2)
if res:
    print(f'{str1} and {str2} are anagrams.')
else:
    print(f'{str1} and {str2} are not anagrams.')