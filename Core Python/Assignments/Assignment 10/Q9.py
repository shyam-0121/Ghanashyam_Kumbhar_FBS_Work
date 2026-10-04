# Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists which will have even elements and other will have odd elements.

def even_odd_list():
    li = []
    n = int(input('Enter number of elements: '))

    for i in range(n):
        num = int(input(f'Enter element {i+1}: '))
        li.append(num)

    even_list = []
    odd_list = []
    size = len(li)

    for j in range(size):
        if li[j] % 2 == 0:
            even_list.append(li[j])
        else:
            odd_list.append(li[j])

    return even_list, odd_list, li

res = even_odd_list()
print(res)