# Python Program to Sum All the Items in a Dictionary

def sum_of_items(d):
    total = 0

    for key in d:
        total += d[key]

    return total

d = {'a' : 10, 'b' : 20, 'c' : 30}
res = sum_of_items(d)
print(res)
