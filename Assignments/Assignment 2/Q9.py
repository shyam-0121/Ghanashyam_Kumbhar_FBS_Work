# Swap two variable without using third variable

x = 11
y = 21

print(f'Before Swapping X:{x}, Y:{y}')

x = x + y
y = x - y
x = x - y

print(f'After Swapping X:{x}, Y:{y}')


