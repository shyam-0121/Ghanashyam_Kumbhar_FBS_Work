# Print list after removing even numbers

def odd_list(li):

    odd = []

    for i in range(len(li)):
        if (li[i] % 2 != 0):
            odd.append(li[i])

    return odd

li = [10, 20, 30, 21, 33, 45, 11, 17]
res = odd_list(li)
print(res)