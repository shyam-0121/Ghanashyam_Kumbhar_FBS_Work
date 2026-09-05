x = 10
y = 10
z = 20

li1 = [10, 20]
li2 = [10, 20]

# 1.is

print( x is y) # True because the immutable value it holds the same memory location.

print( li1 is li2) # False because of the both list holds the different memory location.

# id() function returns the address of the variable.

print(id(x))
print(id(y))

print(id(li1))
print(id(li2))

# If value is mutable you can't reuse it.
# If value is immutable you can reuse it.

# 2. is not

print(x is not y)
print(li1 is not li2)