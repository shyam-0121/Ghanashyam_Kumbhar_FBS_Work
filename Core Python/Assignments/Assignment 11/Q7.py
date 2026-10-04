# Intersection of Two Lists

def intersectio_list(li,li2):

    result = []
    for i in range(len(li)):
        if li[i] in li2:
            result.append(li[i])

    return result
   

li = [10, 20, 30, 40, 50]
li2 = [5, 10, 15, 30, 40, 35, 45, 50]
res = intersectio_list(li,li2)
print(res)