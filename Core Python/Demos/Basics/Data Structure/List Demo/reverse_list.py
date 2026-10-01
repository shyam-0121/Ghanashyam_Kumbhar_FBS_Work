
li = [10,20,30,40,50]

left = 0
right = len(li) - 1

while left < right:
    temp = li[left]
    li[left] = li[right] 
    li[right] = temp
    left += 1
    right -= 1

print(li)