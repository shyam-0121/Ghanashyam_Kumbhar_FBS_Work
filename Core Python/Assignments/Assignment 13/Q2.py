# Python Program to Concatenate Two Dictionaries Into One


def concatenate_two_dict(d1, d2):
    result = {}

    for key in d1:
        result[key] = d1[key]

    for key in d2:
        result[key] = d2[key]

    return result

d1 = {'Name' : 'Shyam', 'Age' : 22}
d2 = {'College' : 'JCJ', 'Course' : 'DS'}
res = concatenate_two_dict(d1, d2)
print(res)