# Check Palindrome

def palindrom_number(n):
    temp = n  
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if temp == reverse:
        print(f'{temp} is a palindrome number.')
    else:
        print(f'{temp} is not a palindrome number.')

n = int(input('Enter Number : '))
palindrom_number(n)  