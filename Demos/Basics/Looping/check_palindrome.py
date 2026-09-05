n = int(input('Enter Number:'))
r = 0
original = n

while n > 0:
    last = n % 10
    r = r * 10 + last
    n = n // 10

if original == r:
    print('Given number is palindrome')
else:
    print('Given number is not a palindrome')



