# # Python Program to Take in a String and Replace Every Blank Space with Hyphen


def replace_with_hypen(Str):
    result = ' '

    for char in Str:
        if char == ' ':
            result += '-'
        else:
            result += char

    return result

String = input('Enter String : ')
res = replace_with_hypen(String)
print(res)
