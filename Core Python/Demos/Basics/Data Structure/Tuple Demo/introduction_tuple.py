# 1. ()
# tup = (10,) # use comma for single value.

# tup = (10, 20, 3.14, "abc",10,10)

# 2 . Heterogenous

# 3. Ordered # Sequence will be maintained.

# 4. Immutable
# tup[0] = 50 # it raises error does not support item assignment

# 5. Duplicate elements are allowed.

# 6. Tuple is fater than the list. Smaller memory block allocation.

import sys

tup = ()
li = []

print(sys.getsizeof(tup))
print(sys.getsizeof(li))


print(tup)