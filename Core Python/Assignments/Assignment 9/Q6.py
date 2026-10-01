# Write a program to print Fibonacci series using recursion.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibonacci(n -1) + fibonacci(n -2)

def print_series(i,n):
    if i == n :
        return
    else :
        print(fibonacci(i))
        print_series(i+1,n)

n = int(input('Enter Number  : '))
print_series(0,n)
