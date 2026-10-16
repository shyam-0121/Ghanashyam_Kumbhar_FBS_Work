# Python Program to Add a Key-Value Pair to the Dictionary

def add_pair(d, key, value):
    d[key] = value
    return d

d = {'Name' : 'Shyam', 'Age' : 22}
key = input('Enter Key : ')
value = input('Enter Value : ')

res = add_pair(d, key, value)
print(res)