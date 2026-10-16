# Python Program to Check if a Given Key Exists in a Dictionary or Not

def check_key_exists(d, key):

    for k in d:
        if k == key:
            return True
        
    
    return False

d = {'Name' : 'Ronaldo', 'Club' : 'Real Madrid', 'Age' : 41}
key = input('Enter Key : ')
res = check_key_exists(d, key)
print(key)

if res:
    print('Key exists')
else:
    print('Key not found')