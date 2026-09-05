# Fibonacci Series

def fibonacci_series(n):
    a = 1
    b = 1

    print("Fibonacci Series:", end=" ")
    for i in range(n):
        print(a, end=' ')
        c = a + b
        a = b
        b = c
    print()  

n = int(input('Enter Number : '))
fibonacci_series(n)