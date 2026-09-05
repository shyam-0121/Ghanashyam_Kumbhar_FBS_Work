# Write a program to check if the given number is positive or negative.

num = int(input('Enter Number:'))

if num > 0:
    print(f'{num} is positive.')
elif num < 0:
    print(f'{num} is negative.')
else:
    print(f'{num} is number zero.')