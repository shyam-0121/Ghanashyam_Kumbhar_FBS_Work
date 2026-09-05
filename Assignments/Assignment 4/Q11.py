# WAP to check if given number is Strong Number

n = int(input('Enter Number : '))
sum = 0
temp = n

while temp > 0 :
    d = temp % 10
    temp = temp // 10

    fact = 1
    for i in range(1,d+1):
        fact *= i
    sum += fact

if sum == n :
    print(f'{n} is strong number.')
else:
    print(f'{n} is not a strong number.')