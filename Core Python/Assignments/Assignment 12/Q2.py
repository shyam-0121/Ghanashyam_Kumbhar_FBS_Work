# Python Program to Remove the nth Index Character from a Non-Empty String

def ind_Str(str,ind):
    result = ''

    for i in range(len(str)):
        if i != ind:
            result += str[i]

    return result

string = input('Enter String : ')
ind = int(input('Enter Index : '))
res = ind_Str(string,ind)
print(res)
