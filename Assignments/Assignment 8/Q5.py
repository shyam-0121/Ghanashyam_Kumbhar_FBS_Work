# Sum of all prime numbers between 1 to n

def sum_of_prime_numbers(n):
    sum = 0

    for num in range(2,n+1):
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            sum += num
    return sum 

n = int(input('Enter Number : '))
result = sum_of_prime_numbers(n)
print('Sum of Prime Numbers : ', result)