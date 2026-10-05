# Python Program to Form a New String where the First Character and the Last Character have been Exchanged

def new_string(str):
    result = ''
    for i in range(len(str)):
        if i == 0:
            result += str[-1]
        elif (i == len(str) - 1):
            result += str[0]
        else:
            result += str[i]

    return result

string = input('Enter String : ')
res = new_string(string)
print(res)        
