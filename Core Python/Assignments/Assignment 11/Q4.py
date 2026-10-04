# Python Program to Find the Second Largest Number in a List Using Bubble Sort.

def second_largest(li):

    for k in range(1, len(li)):
        for j in range(0, len(li) - 1):
            if (li[j] > li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]

    return li[len(li) - 2]

li = [40, 30, 20, 10, 212, 50, 65]

res = second_largest(li)
print(res)