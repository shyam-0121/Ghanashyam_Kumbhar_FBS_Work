# Remove the given key from a dictionary

def remove_key(d, key):

    if key in  d:
        del d[key]
        return 'Key removed successfully'
    else:
        return 'Key not found'

d = {'Name' : 'Shyam', 'Age' : 22}
key = input('Enter Key : ')
res = remove_key(d,key)
print(res)
print(d)
