# Write a program to create a duplicate of an existing list. It should not point to same list.

def duplicate_list(li):
    new_li = []
    size = len(li)

    for i in range(size):
        new_li.append(li[i])

    return new_li

li = [10, 20, 30, 40, 50, 60]
res = duplicate_list(li)
print(res)