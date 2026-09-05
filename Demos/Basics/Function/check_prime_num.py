# Type 1 
# Without passing parameter
# Without returning value

def check_prime():
    n = int(input('Enter Number : '))

    for i in range(2,n):
        if n % i == 0 :
            print(False)
            break

    else:
        print(True)

check_prime()

# Type 2 :
# With passing parameter
# Without returning value

def chk_prime(num):

    for i in range(2,num):
        if num % i == 0 :
            print(False)
            break
    
    else:
        print(True)

num = int(input('Enter Number : '))
chk_prime(num)

# Type 3
# Without pssing parameter 
# With returning value

def check_prime_num():
    isPrime = True

    for i in range(2,number):
        if number % i == 0:
            isPrime = False
            break


    return isPrime

number = int(input('Enter Number : '))
res = check_prime_num()
print('Result : ',res)

# Type 4
# With passing parameter 
# With returning value

def check_prime_number(numm):
    isPrime = True

    for i in range(2,numm):
        if numm % i == 0:
            isPrime = False
            break


    return isPrime

numm = int(input('Enter Number : '))
result = check_prime_number(numm)
print('Result : ',result)