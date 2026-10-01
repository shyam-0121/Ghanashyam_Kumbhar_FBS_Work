# Binary Search 

def binarySearch(li,element):
    beg = 0
    end = len(li) - 1

    while(beg <= end):
        mid = (beg + end) // 2
        if (element ==  li[mid]):
            return mid
        elif (element < li[mid]):
            end = mid - 1
        elif(element > li[mid]):
            beg = mid + 1
    else:
        return -1


li = [10,20,30,40,50,60]
element = int(input('Enter Number to Search : '))
res = binarySearch(li,element)


if res != -1:
    print(f'{element} is present at index {res}.')
else:
    print(f'{element} is not present in the list.')