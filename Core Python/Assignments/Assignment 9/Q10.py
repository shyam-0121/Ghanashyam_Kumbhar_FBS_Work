# Write a program to reverse a number using recursion.

def count_digit(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digit(n // 10)

def reverse_num(n):
    if n < 10:
        return n
    else:
        last = n % 10
        rem = n // 10
        digit = count_digit(rem)
        return last * (10 ** digit) + reverse_num(rem)

n = int(input('Enter Number : '))
res = reverse_num(n)
print(res)