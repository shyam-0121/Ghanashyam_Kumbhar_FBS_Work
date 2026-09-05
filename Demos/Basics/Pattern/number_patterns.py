# i printed 5 times per row
'''
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''
for i in range(1,6):
    for j in range(1,6):
        print(i,end=' ')
    print()

# j printed each row
'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
for i in range(1,6):
    for j in range(1,6):
        print(j,end=' ')
    print()

# Reverse count using range(5,5-i,-1)
'''
4
3 4
2 3 4
1 2 3 4
0 1 2 3 4
'''
for i in range(1,6):
    for j in range(5,5-i,-1):
        print(j, end=' ')
    print()

# Reverse count using range(6-i,0,-1)
'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''
for i in range(1,6):
    for j in range(6-i,0,-1):
        print(j,end=' ')
    print()

# 1/0 checkerboard based on (i+j)
'''
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
'''
for i in range(1,6):
    for j in range(1,6):
        if (i+j) % 2 == 0:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()

# Increasing count per row (1..i)
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# Same row number repeated i times
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

# Multiplication pattern (i*j)
'''
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i*j,end=' ')
    print()

# Continuously increasing number
'''
1 2 3
4 5 6
7 8 9
10 11 12
'''
sum = 1
for i in range(1,5):
    for j in range(1,4):
        print(sum,end=' ')
        sum += 1
    print()

# Hollow square using row number i
'''
1 1 1 1
2     2
3     3
4 4 4 4
'''
for i in range(1,5):
    for j in range(1,5):
        if i == 1 or i == 4 or j == 1 or j == 4:
            print(i,end=' ')
        else:
            print(' ',end=' ')
    print()