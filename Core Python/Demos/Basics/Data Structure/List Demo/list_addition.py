
li = [10,20,30,40,50,60,70]
sum = 0

# Method 1 : Iterating values

for ele in li:
    sum += ele

print(sum)


# Method 2 : Using Indexing
summ = 0
for i in range(0,len(li)):
    summ += li[i]

print('sum : ',summ)