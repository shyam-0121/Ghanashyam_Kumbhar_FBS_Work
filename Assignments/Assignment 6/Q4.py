
for i in range(1,6):
    char = 'A'
    for j in range(1,i+1):
        print(char,end=' ')
        char = chr(ord(char)+1)
    print()