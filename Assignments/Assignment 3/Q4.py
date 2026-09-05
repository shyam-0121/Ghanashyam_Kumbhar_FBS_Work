# Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1 = int(input('Enter Side 1: '))
side2 = int(input('Enter Side 2: '))
side3 = int(input('Enter Side 3: '))

if (side1 > 0 and side2 > 0 and side3 > 0
        and side1 + side2 > side3
        and side2 + side3 > side1
        and side1 + side3 > side2):
    print('Triangle is valid.')
else:
    print('Triangle is not valid.')