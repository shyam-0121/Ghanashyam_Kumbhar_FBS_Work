# Python Program to Calculate the Length of a String Without Using a Library Function

def string_count(Str):
    count = 0

    for char in Str:
        count += 1


    return count

string = input('Enter String : ')
res = string_count(string)
print(res)
