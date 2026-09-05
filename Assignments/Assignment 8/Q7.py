# Sum of digits of a number

def sum_of_digits(n):
    total_sum = 0

    while n > 0:
        digit = n % 10
        total_sum += digit
        n = n // 10

    return total_sum

n = int(input('Enter Number : '))
print('Sum of digits : ',sum_of_digits(n))