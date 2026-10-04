# Write a program to print all numbers which are divisible by m and n in the list.

def divisible_n():
    li = []
    n = int(input('Enter number of Elements : '))
     
    for i in range(n):
        num = int(input(f'Enter Element {i+1}:'))
        li.append(num)

    result = []

    m = int(input('Enter Number M to divide : '))
    n = int(input('Enter Number N to divide : '))

    for i in range(len(li)):
        if(li[i] % m == 0 and li[i] % n == 0):
            result.append(li[i])

    return result

res = divisible_n()
print(res)

