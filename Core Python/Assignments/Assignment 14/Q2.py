# Remove the intersection of a second set with a first set

def rem_intersection(s1, s2):
    for x in s2:
        if x in s1:
            s1.remove(x)

    return s1

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
res = rem_intersection(s1, s2)
print(res)