# Python Program to Merge Two Lists and Sort it.

def merge_sort(li,li2):

    merged = []

    for i in range(len(li)):
        merged.append(li[i])

    for j in range(len(li2)):
        merged.append(li2[j])

    for k in range(1,len(merged)):
        for j in range(0,len(merged) - 1):
            if (merged[j] > merged[j + 1]):
                merged[j] , merged[j + 1] = merged[j + 1] , merged[j]

    return merged

li = [40, 30, 20, 10]
li2 = [5, 15, 25, 35]

res = merge_sort(li,li2)
print(res)