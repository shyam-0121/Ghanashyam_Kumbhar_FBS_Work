# Type 1 
# Without passing parameter
# Without returning value

def check_palindrome():
    n = int(input('Enter Number : '))
    reverse = 0
    temp = n

    while temp > 0 :
        d = temp % 10
        reverse = reverse * 10 + d
        temp = temp // 10

    if n == reverse:
        print(True)
    else:
        print(False)

check_palindrome()

# Type 2 :
# With passing parameter
# Without returning value

def checkPalindrome(n):
    reverse = 0
    temp = n

    while temp > 0 :
        d = temp % 10
        reverse = reverse * 10 + d
        temp = temp // 10

    if n == reverse :
        print(True)
    else:
        print(False)

n = int(input('Enter Number : '))
checkPalindrome(n)

# Type 3
# Without pssing parameter 
# With returning value

def palindrome():
    reverse = 0
    temp = num

    while temp > 0 :
        d = temp % 10
        reverse = reverse * 10 + d
        temp = temp // 10

    if num == reverse :
        return True
    else:
        return False

num = int(input('Enter Number : '))
res = palindrome()
print('Result : ',res)


# Type 4
# With passing parameter 
# With returning value



def palindrome(number):
    reverse = 0
    temp = number

    while temp > 0 :
        d = temp % 10
        reverse = reverse * 10 + d
        temp = temp // 10

    if number == reverse :
        return True
    else:
        return False

number = int(input('Enter Number : '))
result = palindrome(number)
print('Result : ',result)