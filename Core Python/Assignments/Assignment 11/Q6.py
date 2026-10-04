# Python Program to Find the Union of two Lists

def union_list(li,li2):

    merge = []
    for i in range(len(li)):
        merge.append(li[i])

    for j in range(len(li2)):
        merge.append(li2[j])

    final = []

    for i in range(len(merge)):
        if merge[i] not in final:
            final.append(merge[i])

    return final

li = [10, 20, 30, 40, 50]
li2 = [5, 10, 15, 30, 40, 35, 45, 50]
res = union_list(li,li2)
print(res)