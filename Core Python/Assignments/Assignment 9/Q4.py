# Write a program to find sum of n numbers using recursion.

def sum_of_numbers(n):
    sum = 0
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n-1)


n = int(input('Enter Number : '))
result = sum_of_numbers(n)
print(result)