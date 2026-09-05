# Write a program to calculate area of rectangle

def area_of_rectangle(l,b):
    area = l * b
    return area

length = float(input('Enter Length : '))
breadth = float(input('Enter Breadth : '))

area = area_of_rectangle(length,breadth)
print('Area of Rectangle : ',area)