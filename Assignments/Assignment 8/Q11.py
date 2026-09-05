# Check if a given number is an Armstrong number

def armstrongNumber(num):
    temp = num
    sum = 0
    count = 0

    while temp > 0 :
        count += 1
        temp = temp // 10

    temp = num 

    while temp > 0 :
        d = temp % 10
        temp = temp // 10
        sum = sum + (d ** count)

    if sum == num :
        print(f'{num} is a armstrong number.')
    else :
        print(f'{num} is not a armstrong number.')

num = int(input('Enter Number : '))
armstrongNumber(num)
