# Type 1 
# Without passing parameter
# Without returning value

def check_strong():
    n = int(input('Enter Number : '))
    temp = n
    sum = 0

    while temp > 0 :
        d = temp % 10
        temp = temp // 10
        fact = 1
        for i in range(1,d+1):
            fact *= i
        sum += fact

    if sum == n :
        print(True)
    else:
        print(False)

check_strong()

# Type 2 :
# With passing parameter
# Without returning value

def checkStrong(n):
    temp = n
    sum = 0
    
    while temp > 0 :
        d = temp % 10
        temp = temp // 10
        fact = 1
        for i in range(1,d+1):
            fact *= i
        sum += fact
    
    if sum == n :
        print(True)
    else:
        print(False)

n = int(input('Enter Number : '))
checkStrong(n)

# Type 3
# Without pssing parameter 
# With returning value


def check_strong_num():
    temp = num 
    sum = 0

    while temp > 0 :
        d = temp % 10
        temp = temp // 10
        fact = 1
        for i in range(1,d+1):
            fact *= i
        sum += fact

    if sum == num :
        return True
    else:
        return False

num = int(input('Enter Number : '))
res = check_strong_num()
print('Result : ',res)

# Type 4
# With passing parameter 
# With returning value

def strongNumber(number):
    temp = number
    sum = 0

    while temp > 0 :
        d = temp % 10
        temp = temp // 10
        fact = 1
        for i in range(1,d+1):
            fact *= i
        sum += fact

    if number == sum :
        return True
    else:
        return False

number = int(input('Enter Number : '))
result = strongNumber(number)
print('Result : ',result)

