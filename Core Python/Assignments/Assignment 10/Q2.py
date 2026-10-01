# Write a program to find maximum and minimum element in a list.

def min_max(li):
    mini = li[0]
    maxi = li[0]

    for i in range(0, len(li)):
        if li[i] > maxi:
            maxi = li[i]

    for i in range(1, len(li)):
        if mini > li[i]:
            mini = li[i]

    return maxi, mini


li = [50, 40, 60, 70, 10]
maxi, mini = min_max(li)
print(f"Maximum: {maxi}, Minimum: {mini}")
