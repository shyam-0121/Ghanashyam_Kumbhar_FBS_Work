
# li = [[10,20], [30,40], [50,60]]

# total = 0

# for i in li:
#     # print(i)
#     for j in i:
#         # print(j)
#         total += j

# print(total)

li2 = [5,[10,20], [30,40], [50,60], [10,20],10,20]
total = 0

for i in li2:
    if isinstance(i,list):
        for j in i:
            print(total)
            total += j
    else:
        total += i

print(total)

