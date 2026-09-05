'''
        * 
      *   * 
    *       * 
  *           * 
*               * 
*               * 
  *           * 
    *       * 
      *   * 
        * 

'''

# Top half
for i in range(1, 6):
    for j in range(1, 6-i):
        print(' ', end=' ')
    if i == 1:
        print('*', end=' ')
    else:
        print('*', end=' ')
        for j in range(1, 2*i-2):
            print(' ', end=' ')
        print('*', end=' ')
    print()

# Bottom half (mirrors all 5 rows, including widest)
for i in range(5, 0, -1):
    for j in range(1, 6-i):
        print(' ', end=' ')
    if i == 1:
        print('*', end=' ')
    else:
        print('*', end=' ')
        for j in range(1, 2*i-2):
            print(' ', end=' ')
        print('*', end=' ')
    print()