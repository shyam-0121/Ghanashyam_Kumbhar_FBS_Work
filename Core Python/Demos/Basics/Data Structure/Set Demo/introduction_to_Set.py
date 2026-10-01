# 1. {}

s1 = set() # To create the empty set

# 2 . Heterogeneous
s1 = {10,20,30,3.14, 10, 20}

# 3. Unordered 

# 4. Mutable , but not editable

# 5. Unique elements are allowed.
s1.add(50)
print(s1)

total = 0

for ele in s1:
    total += ele

print(total)
