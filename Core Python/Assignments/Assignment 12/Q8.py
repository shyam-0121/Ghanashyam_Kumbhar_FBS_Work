# Python Program to Remove the Characters of Odd Index Values in a String

def even_String(Str):
    result = ''

    for i in range(len(Str)):
        if i % 2 == 0:
            result += Str[i]

    return result

string = input('Enter String : ')
res = even_String(string)
print(res)