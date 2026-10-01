# Write a program to reverse a given number using recursive function.

def count_digit(n):
    count = 0
    if (n < 10):
        return 1
    else:
        count = 1 + count_digit(n//10)

    return count

def reverse_num(n):
    if n < 10 :
        return n 
    else :
        last = n % 10
        rem = n // 10
        digit = count_digit(rem)

    return last*(10 ** digit ) + reverse_num(rem)

n = int(input('Enter Number  : '))
res = reverse_num(n)
print(res)