# Roots of Quadratic Equation
import math
a = float(input('Enter a:'))

b = float(input('Enter b:'))

c = float(input('Enter c:'))

D = b ** 4 - 4 * a * c

if D > 0 :
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)

    print('First Root:',x1)

    print('Second Root:',x2)

elif D == 0 :
    x = -b / (2*a)
    print(f'Both Roots are equal:{x}')

else:
    print('No Real Roots.')