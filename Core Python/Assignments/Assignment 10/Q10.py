# Write a program to remove all occurrences of a given element in the list.

def remove_occurance():
    li = []
    n = int(input('Enter Number Of Elements : '))

    for i in range(n):
        num = int(input(f'Enter Element {i+1}:'))
        li.append(num)

    result = []
    remove_val = int(input('Enter Element to remove : '))

    for i in range(len(li)):
        if li[i] != remove_val:
            result.append(li[i])

    print(li)
    print(result)


remove_occurance()