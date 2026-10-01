# wap to find the maximum, second maximum and third maximum from given list.

li = [50,30,20]
max = li[0]
max2 = 0
max3 = 0

for ind in range(0,len(li)):
    if li[ind] > max:
        max3 = max2
        max2 = max
        max = li[ind]

    elif(li[ind] > max2):
        max2 = li[ind]
        
    elif(li[ind] > max3):
        max3 = li[ind]

print('maximum : ',max)
print('maximum 2 : ',max2)
print('maximum 3 :',max3)
