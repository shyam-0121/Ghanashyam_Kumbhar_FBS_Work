# Write a program to check if given number is Armstrong number or not

n = int(input('Enter Number : '))
temp = n
count = 0
sum = 0

while temp > 0 :
    count += 1
    temp = temp // 10

temp = n
while temp > 0 :
    d = temp % 10
    sum = sum + (d ** count)
    temp = temp // 10

if sum == n :
    print(f'{n} is a armstrong number.')
else:
    print(f'{n} is not a armstrong number.')