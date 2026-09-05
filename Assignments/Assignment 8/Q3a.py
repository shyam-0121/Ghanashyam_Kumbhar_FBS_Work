# Find the sum 1 + 2 + 3 + 4 + ... + n

def sum_of_series(n):
    sum = 0

    for i in range(1,n+1):
        sum += i
    print('Sum of Series : ',sum)


n = int(input('Enter Number : '))
sum_of_series(5)
