# Type 1 
# Without passing parameter
# Without returning value

def perfect_num():
    num = int(input('Enter Number : '))
    sum = 0

    if num <= 0 :
        print(False)
        return

    for i in range(1,num):
        if num % i == 0 :
            sum += i

    if sum == num:
        print(True)
    else:
        print(False)

perfect_num()    


# Type 2 :
# With passing parameter
# Without returning value

def check_perfect(n):
    if n <= 0 :
        print(False)
        return

    sum = 0

    for i in range(1,n):
        if n % i == 0 :
            sum += i

    if sum == n :
        print(True)
    else:
        print(False)

n = int(input('Enter Number : '))
check_perfect(n)

# Type 3
# Without pssing parameter 
# With returning value

def perfect_number():
    if number <= 0 :
        return False
    
    sum = 0

    for i in range(1,number):
        if number % i == 0 :
            sum += i

    if number == sum :
        return True
    else :
        return False

number = int(input('Enter Number : '))
res = perfect_number()
print('Result : ',res)


# Type 4
# With passing parameter 
# With returning value

def check_perfect_number(numm):
    if numm <= 0 :
        return False

    sum = 0

    for i in range(1,numm):
        if numm % i == 0 :
            sum += i

    if numm == sum :
        return True
    else :
        return False

numm = int(input('Enter Number : '))
result = check_perfect_number(numm)
print('Result : ',result)
