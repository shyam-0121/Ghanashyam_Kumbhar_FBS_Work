# armstrong number

num = int(input('Enter Number:'))

temp = num
count = 0

sum = 0

# count digits
while temp > 0:
    count +=1
    temp = temp // 10

# Calculate armstrong

temp = num
while temp > 0:
    d = temp % 10
    temp = temp // 10
    sum = sum + (d ** count)

# check is it armstrong or not

if sum == num:
    print(f'{num} is a armstrong number.')
else:
    print(f'{num} is not a armstrong number.')