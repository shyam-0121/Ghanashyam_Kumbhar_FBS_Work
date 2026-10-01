import copy

li1 = [10, 20, [30, 40]]

# copy.copy() creates a shallow copy.
# The outer list is new, but nested objects are shared.
li2 = copy.copy(li1)

# li1 and li2 are different outer list objects,
# so their IDs will be different.
print(id(li1))
print(id(li2))

# Changing a top-level element of li1.
# li2 will NOT be affected because the outer lists are separate.
li1[1] = 111

# Changing a top-level element of li2.
# li1 will NOT be affected for the same reason.
li2[1] = 999

print(li1)   # [10, 111, [30, 40]]
print(li2)   # [10, 999, [30, 40]]