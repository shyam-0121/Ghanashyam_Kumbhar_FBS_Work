# Sum of series 1! + 2! + 3! + ... + n! using recursive functions

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

def sum_of_series(n):
    if n == 0:
        return n
    else:
        return fact(n) + sum_of_series(n-1)

n = int(input('Enter Number : '))
result = fact(n)
print('Result : ',result)
res = sum_of_series(n)
print('Result : ', res)
