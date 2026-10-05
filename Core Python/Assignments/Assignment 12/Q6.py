# Python Program to Take in a String and Replace Every Blank Space with Hyphen

def replce_with_hyphen(Str):
    result = ''

    for char in Str:
        if char == ' ':
            result += '-'
        else:
            result += char

    return result

String = input('Enter String : ')
res = replce_with_hyphen(String)
print(res)