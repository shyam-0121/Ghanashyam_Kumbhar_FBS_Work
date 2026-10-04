def snake_ladder():
    num = 1
    for row in range(10):
        if row % 2 == 0:
            for col in range(10):
                print(num, end='\t')
                num += 1
        else:
            temp = []
            for col in range(10):
                temp.append(num)
                num += 1
            for i in range(len(temp)-1, -1, -1):
                print(temp[i], end='\t')
        print()

snake_ladder()