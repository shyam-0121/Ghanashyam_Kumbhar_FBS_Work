# reverse the list

def reverse_list(li):
    left = 0
    right = len(li) - 1

    while left < right:
        temp = li[left]
        li[left] = li[right]
        li[right] = temp

        left += 1
        right -= 1

li = [50, 40, 30, 20, 10]
reverse_list(li)
print(li)