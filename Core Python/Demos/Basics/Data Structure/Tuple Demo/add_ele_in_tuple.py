
tup = (10, 20, 30, 40, 60)

li = list(tup)

li.insert(4,50)
li.append(70)
li.extend(([80,90,100]))

tup = tuple(li)
print(tup)
print(type(tup))