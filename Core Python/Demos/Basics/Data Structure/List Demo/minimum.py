
li = [20,10,3,50,40,212,50,60]

min = li[0]
min2 = 0


for ind in range(1,len(li)):
    if min > li[ind] :
        min2 = min
        min = li[ind]

print('minimum : ',min)
print('minimum 2 :',min2)