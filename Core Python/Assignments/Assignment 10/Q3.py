# Second largest element

def second_large(li):
    maxi = li[0]
    second_max = None

    for i in range(1, len(li)):
        if li[i] > maxi:
            second_max = maxi
            maxi = li[i]
        elif li[i] != maxi and (second_max is None or li[i] > second_max):
            second_max = li[i]

    return second_max


li = [-1, -8]
res = second_large(li)
print('Second Max :', res)