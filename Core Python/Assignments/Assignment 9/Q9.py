# Write a program to calculate m to the power n using recursion.

def power(m,n):
    if n == 0 :
        return 1
    else :
        return m * power(m,n-1)

n = int(input('Enter Number : '))
res = power(3,n)
print(res)