# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x, x*x)

def dict_nums(n):
    result = {}

    for x in range(1, n+1):
        result[x] = x * x

    return result

n = int(input('Enter Number : '))
res = dict_nums(n)
print(res)