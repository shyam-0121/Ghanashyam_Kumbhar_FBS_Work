# Write a program to create three lists of numbers, their squares and cubes.

def squares_cubes():
    li = []
    n = int(input('Enter Number of Elements : '))
    for i in range(n):
        num = int(input('Enter Elements : '))
        li.append(num)

    cubes = []
    for j in range(len(li)):
        cubes.append(li[j] ** 3)

    squares = []
    for k in range(len(li)):
        squares.append(li[k] ** 2)


    return squares,cubes

res = squares_cubes()
print(res)