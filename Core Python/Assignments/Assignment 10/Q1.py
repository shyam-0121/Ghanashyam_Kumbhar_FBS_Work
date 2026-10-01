# Sum of all elements

def sum_of_elements(li):
    total = 0

    for i in li:
       total += i

    return total

li = [50, 40, 20, 10, 30]
res = sum_of_elements(li)
print('Sum : ',res)