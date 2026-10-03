# Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

def num_of_elements(num):
    count = 0
    size = len(li)

    for i in range(size):
        if li[i] == num:
            count += 1

    return count


li = [20, 3, 40, 50, 65, 10, 30]
num = int(input('Enter Number :'))
res = num_of_elements(num)

if res > 0:
    print(f'{num} is present {res} times.')
else:
    print(f'{num} is not present.')