# Write a function which we pass a parameter and print the factors of given number.

def factors_of_num(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(i)

factors_of_num(12)