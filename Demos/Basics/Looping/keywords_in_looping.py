# 1. pass: it neglects the identation error.
for i in range(1,11):
    pass


# 2. break: it terminates the loop.
for k in range(1,11):
    if k == 4:
        break
    print(k)


# 3. continue: it skips the particular iteration like if condition satisfies.
for j in range(1,11):
    if j == 4:
            continue
    print(j)

# 4. else: will excute when loop excuted successfully.
for y in range(1,11):
     if y == 4:
          continue
else:
     print('Loop excuted...')


