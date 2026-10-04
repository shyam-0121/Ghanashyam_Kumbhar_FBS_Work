# Python Program to Sort the List According to the Second Element in Sublist.

def sort_by_second(li):

    for k in range(1, len(li)):
        for j in range(0, len(li) - 1):
            if (li[j][1] > li[j + 1][1]):
                li[j], li[j + 1] = li[j + 1], li[j]

    return li

li = [[1, 5], [2, 3], [3, 9], [4, 1]]

res = sort_by_second(li)
print(res)