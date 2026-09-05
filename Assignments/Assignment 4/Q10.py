# WAP to check if a given number is a Perfect Number

n = int(input('Enter Number : '))
sum = 0

for i in range(1,n):
    if n % i == 0:
        sum += i

if sum == n :
    print(f'{n} is perfect number.')
else:
    print(f'{n} is not a perfect number.') 