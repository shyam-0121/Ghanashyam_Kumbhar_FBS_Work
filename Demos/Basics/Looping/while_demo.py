# while(condition):
    # block of code

# 1. Variable Inititalization
# 2. Variable Used in condition
# 3. Value should be change (increment / decrement)


#i = 0
#while(i < 5):
#    print('Hello Shyam..!')
#   i += 1


#num = 1

#while(num < 11):
#    print(num)
#    num += 1

sum = 0
number = int(input('Enter Number:'))
while(number > 0):
    d = number % 10
    print(d,end = ' ')
    sum += d
    number = number // 10

print(f'sum:{sum}')
    


