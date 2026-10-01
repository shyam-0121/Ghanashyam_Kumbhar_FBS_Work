import copy

li1 = [10, 20, [30, 40]]

# deepcopy() creates a completely independent copy,
# including the nested list [30, 40].
li2 = copy.deepcopy(li1)

# Changing the nested list of li1.
# Because li2 is a deep copy, li2 will NOT be affected.
li1[2][0] = 999

# li1 and li2 have different outer-list memory addresses.
print(id(li1))   # Different ID
print(id(li2))   # Different ID

# Original list is changed.
print(li1)       # [10, 20, [999, 40]]

# Deep copy remains unchanged.
print(li2)       # [10, 20, [30, 40]]