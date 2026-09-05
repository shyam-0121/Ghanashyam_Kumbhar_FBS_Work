# 1! + 2! + 3! + 4! + ... + n!

def sum_of_fact(n):
    sum = 0
    fact = 1

    for i in range(1,n+1):
        fact *= i
        sum += fact

    return sum

n = int(input('Enter Number : '))
print('Sum of factorial:',sum_of_fact(n))