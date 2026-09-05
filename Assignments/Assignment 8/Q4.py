# Sum of all odd numbers between 1 to n

def sum_of_odd_numbers(n):
    sum = 0

    for i in range(1,n+1):
        if i % 2 == 0:
            continue
        else:
            sum += i

    return sum

n = int(input('Enter Number : '))
result = sum_of_odd_numbers(n)
print('Sum of odd numbers : ',result)