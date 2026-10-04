# Python Program to Sort a List According to the Length of the Elements within the list


def sort_by_length(li):

    for k in range(1, len(li)):
        for j in range(0, len(li) - 1):
            if (len(li[j]) > len(li[j + 1])):
                li[j], li[j + 1] = li[j + 1], li[j]

    return li

li = ["banana", "kiwi", "apple", "fig"]

res = sort_by_length(li)
print(res)