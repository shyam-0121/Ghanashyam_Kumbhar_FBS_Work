# Type 1 
# Without passing parameter
# Without returning value

def armstrong():
    n = int(input('Enter Number : '))
    temp = n
    sum = 0
    count = 0

    while temp > 0 :
        count += 1
        temp = temp // 10

    temp = n
    while temp > 0 :
        d = temp % 10
        temp = temp // 10
        sum = sum + (d ** count)


    if sum == n :
        print(True)
    else :
        print(False)

armstrong()

# Type 2 :
# With passing parameter
# Without returning value

def check_armstrong(n):
    sum = 0
    temp = n
    count = 0

    while temp > 0 :
        count += 1
        temp = temp // 10

    temp = n
    while temp > 0 :
        d = temp % 10
        temp = temp // 10
        sum = sum + (d ** count)

    if sum == n :
        print(True)
    else:
        print(False)

n = int(input('Enter Number : '))
check_armstrong(n)


# Type 3
# Without pssing parameter 
# With returning value

def armStrong():
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
        return True
    else:
        return False

num = int(input('Enter Number : '))
res = armStrong()
print('Result : ',res)


# Type 4
# With passing parameter 
# With returning value

def check_armstrong_num(number):
    sum = 0
    temp = number
    count = 0

    while temp > 0 :
        count += 1
        temp = temp // 10

    temp = number

    while temp > 0 :
        d = temp % 10
        temp = temp // 10
        sum = sum + (d ** count)

    if sum == number :
        return True
    else:
        return False

number = int(input('Enter Number : '))
result = check_armstrong_num(number)
print('Result : ',result)