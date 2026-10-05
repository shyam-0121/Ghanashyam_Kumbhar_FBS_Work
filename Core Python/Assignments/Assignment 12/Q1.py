# Python Program to Replace all Occurrences of 'a' with $ in a String

def replacing(str):

    result = ''
    for char in str:
        if char == 'a':
            result += '$'
        else:
            result += char

    return result

str = input('Enter String : ')
res = replacing(str)
print(res)