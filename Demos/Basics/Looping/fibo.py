a = 0
b = 1
num = int(input('Enter number:'))

for i in range(num):
    c = a + b
    a = b
    b = c

    i += 1

    print(a)

print('funtion call')

def fibo(n):
    x = 0
    y = 1

    for _ in range (n):
        print(x, end=" ")
        z = x + y
        x = y
        y = z
        

fibo(6)


