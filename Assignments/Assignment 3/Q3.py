# Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 = int(input('Enter Angle 1 :'))
angle2 = int(input('Enter Angle 2 :'))
angle3 = int(input('Enter Angle 3 :'))


if angle1 > 0 and angle2 > 0 and angle3 > 0 and angle1 + angle2 + angle3 == 180:
    print('Triangle Is Valid.')
else:
    print('Triangle is not Valid')