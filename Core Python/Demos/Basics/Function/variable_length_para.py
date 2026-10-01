# 1 . To pass multiple para to function
# 2 . Mention asterisk(*) symbol before  para in function definition
# 3 . Values will be stored in the tuple format.
# 4 . Use for loop to iterate values from tuple.

def addition(*num):
    print(type(num))
    print(num)
    sum = 0
    for val in num:
        sum += val
    return sum


res = addition(10,20,30,40,50)
print('Result : ',res)