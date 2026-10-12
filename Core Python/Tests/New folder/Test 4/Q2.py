# Write a program to find the factorial of given number using recursion.


def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)

print(fact(5))