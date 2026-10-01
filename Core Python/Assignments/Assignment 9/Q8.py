# Write a program to check whether a number is prime or not using recursion.

def is_Prime(n,i):
    if i >= n :
        return True

    if n % i == 0 :
        return False
    else :
        return is_Prime(n, i+1)

n = int(input('Enter Number : '))
res = is_Prime(n,2)
print(res)