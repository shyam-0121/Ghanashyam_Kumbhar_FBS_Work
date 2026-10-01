# Linear search

def linearSearch(li,element):
    size = len(li)

    for ind in range(0,size):
        if li[ind] == element:
            return ind
    else:
        return -1


li = [20,30,40,55,61]
element = int(input('Enter Number To Search : '))
res = linearSearch(li,element)

if res != -1:
    print(f'{element} is present at index {res}.')
else:
    print(f'{element} is not present in the list.')