# Write a program to create three lists of numbers, their squares and cubes

def square_cube(li):
    square = []
    cube = []

    for i in range(len(li)):
        square.append(li[i] ** 2)

    for j in range(len(li)):
        cube.append(li[j] ** 3)

    return square, cube

li = [10, 20, 30, 40, 50]
square, cube = square_cube(li)
print('Square : ',square)
print('Cube : ',cube)