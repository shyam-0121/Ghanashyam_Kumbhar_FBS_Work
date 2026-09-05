# Reverse a Three digit number

num = 578

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

reverse_digit = (d1 * 100) + (d2 * 10) + d3

print(f'Reverse a Three-Digits:{reverse_digit}')