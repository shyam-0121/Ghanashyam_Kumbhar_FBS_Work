# Python Program to Put Even and Odd elements of a List into two Different Lists

def even_odd(li):

    size = len(li)

    even = []
    odd = []

    for i in range(size):
        if (li[i] % 2 == 0):
            even.append(li[i])
        else:
            odd.append(li[i])

    return even,odd

li = [10, 21, 30, 41, 50, 61]
even, odd = even_odd(li)

print('even =', even)
print('odd =', odd)