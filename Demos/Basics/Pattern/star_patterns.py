# Simple 5x5 star grid
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
for i in range(1,6):
    for j in range(1,6):
        print('*',end=' ')
    print()

# Right triangle (increasing)
'''
*
* *
* * *
* * * *
* * * * *
'''
for i in range(1,6):
    for j in range(1,i+1):
        print('*', end=' ')
    print()

# Right triangle (decreasing)
'''
* * * * *
* * * *
* * *
* *
*
'''
for i in range(1,6):
    for j in range(1,7-i):
        print('*', end=' ')
    print()

# Alternating * and $ by row
'''
* * * * *
$ $ $ $ $
* * * * *
$ $ $ $ $
* * * * *
'''
for i in range(1,6):
    for j in range(1,6):
        if i % 2 == 0:
            print('$',end=' ')
        else:
            print('*',end=' ')
    print()

# Checkerboard: * or $ based on (i+j)
'''
$ * $ * $
* $ * $ *
$ * $ * $
* $ * $ *
$ * $ * $
'''
for i in range(1,6):
    for j in range(1,6):
        if (i+j) % 2 == 0:
            print('*',end=' ')
        else:
            print('$',end=' ')
    print()

# Checkerboard: $ or * (reversed condition)
'''
* $ * $ *
$ * $ * $
* $ * $ *
$ * $ * $
* $ * $ *
'''
for i in range(1,6):
    for j in range(1,6):
        if (i+j) % 2 == 0:
            print('$',end=' ')
        else:
            print('*',end=' ')
    print()

# Hollow square (fixed 7x7)
'''
* * * * * * *
*           *
*           *
*           *
*           *
*           *
* * * * * * *
'''
for i in range(1,8):
    for j in range(1,8):
        if i == 1 or i == 7 or j == 1 or j == 7:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

# Left-aligned pyramid
'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
for i in range(1,6):
    for j in range(1,6-i):
        print(' ', end=' ')
    for j in range(1,i+1):
        print('*', end=' ')
    print()

# Right-aligned inverted triangle
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''
for i in range(1,6):
    for j in range(1,i):
        print(' ',end=' ')
    for j in range(1,7-i):
        print('*',end=' ')
    print()

# Hollow square from user input
'''
Enter Row: 5
* * * * *
*       *
*       *
*       *
* * * * *
'''
n = int(input('Enter Row:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

# full pyramid
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

for i in range(1,6):

    for j in range(1,6 - i):
        print(' ', end=' ')

    for j in range(1,2*i):
        print('*', end=' ')

    print()

# hollow pyramid

'''
        *
      *   *
    *       *
  *           *
* * * * * * * * *
'''
for i in range(1, 6):

    for j in range(1, 6-i):
        print(' ',end=' ')

    if i == 1:
        print('*',end=' ')

    elif i == 5:
        for j in range(1,2*i):
            print('*',end=' ')
    else:
        print('*', end=' ')

        for j in range(1, 2*i-2):
            print(' ', end=' ')

        print('*', end=' ')

    print()

'''
* * * * *
*       *
*       *
*       *
* * * * *

'''

for i in range(1,6):
    for j in range(1,6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''
*
* *
*   *
*     *
* * * * *

'''

for i in range(1,6):
    for j in range(1,i + 1):
        if i == 5 or j == 1 or i == j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


'''
* * * * *
*     *
*   *
* *
*
'''

for i in range(1,6):
    for j in range(1,7-i):
        if i == 1 or j == 1 or i + j == 6:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


'''
* * * * *
  * * * * 
    * * *
      * *
        *
'''

for i in range(1,6):
    for j in range(1,i):
        print(' ',end=' ')
    for j in range(1,7-i):
        print('*',end=' ')

    print()

'''
     *
'''

for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()

'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * *     
'''

for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,2*i):
        print('*',end=' ')

    print()


'''
        *   
      *   *   
    *   *   *   
  *   *   *   *   
*   *   *   *   *  
'''

for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1, i + 1):
        print('*  ',end=' ')

    print()


'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

'''

for i in range(1,6):
    for j in range(1,i + 1):
        print('*',end=' ')
    print()

for i in range(1,5):
    for j in range(1,6-i):
        print('*',end=' ')
    print()



'''

'''
print('pattern')
for i in range(1,6):
    for j in range(1,i + 1):
        print('*',end=' ')
    print()

for i in range(1,5):
    for j in range(1,5-i):
        print('*',end=' ')

print()
print()
k = 7

for i in range(1,6):
    for j in range(1, i+1):
        print('*',end=' ')

    for j in range(1, k + 1):
        print(' ',end=' ')
    k -= 2

    for j in range(1,i+1):
        if (i!=5 or j!=5):
            print("*",end=" ")
       
    print()


for i in range(1,5):
    for j in range(1,i+1):
        print('*',end=' ')
    for j in range(1,5-i):
        print(' ',end=' ')
    print()


for i in range(1,6):
    for j in range(5,i-1):
        print(j,end=' ')
    print()


