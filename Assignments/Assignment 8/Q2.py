# Calculate the area of circle

def area_of_circle(r):
    area = 3.14 * r * r
    return area

radius = float(input('Enter Radius : '))
area = area_of_circle(radius)
print('Area of Circle : ',area)