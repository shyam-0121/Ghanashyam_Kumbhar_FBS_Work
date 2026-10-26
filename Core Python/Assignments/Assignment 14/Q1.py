
# Find the elements in a given set that are not in another set

def find_ele(s1, s2):
    result = set()

    for x in s1:
        if x not in s2:
            result.add(x)

    return result

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
res = find_ele(s1, s2)
print(res)
         