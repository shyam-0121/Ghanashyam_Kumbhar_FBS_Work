# Write a program to print list after removing even numbers.

def odd_list(li):

    size = len(li)
    result = []

    for i in range(size):
        if (li[i] % 2 != 0):
            result.append(li[i])

    return result

li = [10, 20, 33, 40, 50, 67, 78, 95]
res = odd_list(li)
print(res)
