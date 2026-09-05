# AAAA BBBB CCCC using chr(ord)
'''
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
'''
char = 'A'
for i in range(1,6):
    for j in range(1,6):
        print(char,end=' ')
    print()
    char = chr(ord(char)+1)

# Using string 'ABCDE'
'''
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
'''
s = 'ABCDE'
for i in range(5):
    for j in range(5):
        print(s[i],end=' ')
    print()

# Using a list ['A','B','C','D','E']
'''
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
'''
li = ['A','B','C','D','E']
for i in range(5):
    for j in range(5):
        print(li[i], end=' ')
    print()

# Using chr(65..68) directly (ASCII)
'''
A A A A
B B B B
C C C C
D D D D
'''
for i in range(65,69):
    for j in range(4):
        print(chr(i), end=' ')
    print()