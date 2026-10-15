# Count the number of lowercase characters in a string

def count_lowercase(String):
    count = 0

    for char in String:
        if char >= 'a' and char <= 'z':
            count += 1

    return count

String = input('Enter String : ')
res = count_lowercase(String)
print(res)
