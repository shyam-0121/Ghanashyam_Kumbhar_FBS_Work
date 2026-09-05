# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input("Enter x: "))
n = int(input("Enter number of terms: "))
sum = 0
sign = 1

for i in range(1, n+1):
    denominator = 2*i - 1
    sum += sign * (x ** i) / denominator
    sign = sign * -1

print("Sum of series:", sum)