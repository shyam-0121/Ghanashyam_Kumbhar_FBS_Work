li = [50, 20, 30, 40, 90, 47, 50, 50]


# --------------------------------------------------
# 1. append()
# --------------------------------------------------
# Adds ONE element at the end of the list.
# Returns None.

li.append(60)
print(li)


# --------------------------------------------------
# 2. clear()
# --------------------------------------------------
# Removes ALL elements from the list.
# Returns None.

# li.clear()
# print(li)


# --------------------------------------------------
# 3. copy()
# --------------------------------------------------
# Creates a SHALLOW COPY of the list.
# Original and copied list have different IDs.

li2 = li.copy()

print(li2)
print(id(li))
print(id(li2))


# --------------------------------------------------
# 4. Assignment (=)
# --------------------------------------------------
# Does NOT create a new list.
# Both variables point to the SAME list.

li3 = li

print(id(li))
print(id(li3))


# --------------------------------------------------
# 5. count()
# --------------------------------------------------
# Counts how many times an element occurs.

print(li.count(50))


# --------------------------------------------------
# 6. extend()
# --------------------------------------------------
# Adds MULTIPLE elements to the end of the list.
# Returns None.

li.extend([20, 30, 40])
print(li)


# --------------------------------------------------
# 7. index()
# --------------------------------------------------
# Returns the index of the FIRST occurrence
# of the specified element.

print(li.index(50))


# --------------------------------------------------
# 8. insert()
# --------------------------------------------------
# Inserts an element at a specific index.
# Syntax: list.insert(index, value)
# Returns None.

li.insert(0, 10)
print(li)


# --------------------------------------------------
# 9. remove()
# --------------------------------------------------
# Removes the FIRST occurrence of a specified VALUE.
# Returns None.

li.remove(50)
print(li)


# --------------------------------------------------
# 10. pop()
# --------------------------------------------------
# Removes and RETURNS an element.
# By default, removes the LAST element.
# pop(index) removes the element at that index.

removed = li.pop()
print(removed)
print(li)


# --------------------------------------------------
# 11. reverse()
# --------------------------------------------------
# Reverses the list in-place.
# Returns None.

li.reverse()
print(li)


# --------------------------------------------------
# 12. sort()
# --------------------------------------------------
# Sorts the list in ascending order by default.
# reverse=True sorts in descending order.
# Returns None.

li.sort(reverse=True)
print(li)


