for i in range(1, 6):
    for j in range(1, 6-i):
        print(' ', end=' ')

    if i == 1:
        print('1', end=' ')
    elif i == 5:
        for k in range(1, 6):
            print(k, end=' ')
    else:
        print('1', end=' ')
        for j in range(1, 2*i-2):
            print(' ', end=' ')
        print(i, end=' ')

    print()