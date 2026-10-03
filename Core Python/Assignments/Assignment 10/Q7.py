# Write a program to create a new list from existing list which contains cube of each number of list.

def cube_of_ele(li):
    cube = []
    size = len(li)

    for i in range(size):
        cube.append(li[i]**3)

    return cube

li = [10, 20, 30, 40]
res = cube_of_ele(li)
print(res)