# c. Find the sum of a geometric series from 1 to n where the common ratio is 2

n = int(input("Enter n: "))
sum = 0
term = 1

for i in range(n):
    sum += term
    term = term * 2

print("Sum of series:", sum)