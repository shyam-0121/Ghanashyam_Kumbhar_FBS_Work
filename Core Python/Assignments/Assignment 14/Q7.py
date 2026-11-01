# Given two sets of numbers, find the missing numbers in the second set as compared to the first and vice versa (use the Python set)

def find_missing(s1, s2):

    set1 = set()
    set2 = set()

    for x in s1:
        if x not in s2:
            set1.add(x)

    for x in s2:
        if x not in s1:
            set2.add(x)

    return set1, set2

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}
set1, set2 = find_missing(s1, s2)
print(set1)
print(set2)
