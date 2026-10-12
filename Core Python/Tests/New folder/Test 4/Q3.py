# Print the following program.
witdth = 22
rows = 10

for i in range(rows):
    if i == 0 or i == rows - 1:
        print('*' * witdth)
    else:
        space = witdth - 1 - i * 2
        print(' '* space + '*')