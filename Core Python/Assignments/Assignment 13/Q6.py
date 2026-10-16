# Python Program to Multiply All the Items in a Dictionary

def multiply_all_items(d):
    total = 1

    for key in d:
        total *= d[key]

    return total

d = {'a' : 2, 'b' : 5, 'c' : 10}
res = multiply_all_items(d)
print(res)