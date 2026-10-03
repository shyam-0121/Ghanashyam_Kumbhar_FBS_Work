 # Write a program to remove duplicates from the list.

def rm_duplicates(li):
    result = []
    size = len(li)

    for i in range(size):
        if li[i] not in result:
            result.append(li[i])

    print(result)


li = [10, 20, 30, 50, 10, 20, 30, 40, 50]
rm_duplicates(li)