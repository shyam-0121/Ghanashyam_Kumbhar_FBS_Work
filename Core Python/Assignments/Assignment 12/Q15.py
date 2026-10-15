# Python Program to find larger string without using built-in functions

def larger_string(Str1, Str2):
    count1 = 0
    count2 = 0

    for i in Str1:
        count1 += 1

    for j in Str2:
        count2 += 1

    if count1 > count2:
        return f'{Str1} : String 1 is largest.'
    elif count2 > count1:
        return f'{Str2} : String 2 is largest.'
    else:
        return 'Both strings are equal'

Str1 = input('Enter String 1 : ')
Str2 = input('Enter String 2 : ')

res = larger_string(Str1, Str2)
print(res)