# 1¹ + 2² + 3³ + 4⁴ + ... + nⁿ

def sum_of_powers(n):
    sum = 0
    for i in range(1,n+1):
        sum += i ** i
    return sum

n = int(input('Enter Number : '))
result = sum_of_powers(n)
print('Sum of Powers : ',result)