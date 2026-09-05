# Write a program to check if given 3 digit number is a palindrome or not

num = int(input('Enter Number :'))

temp = num
reverse = 0

while temp > 0:
    last = temp % 10
    reverse = reverse * 10 + last
    temp = temp // 10

if reverse == num :
    print(f'{num} is a palindrom.')
else:
    print(f'{num} is not a palindrome')