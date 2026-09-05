# WAP to print Armstrong number within a given range

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for n in range(start, end+1):
    temp = n
    count = 0
    sum = 0

    while temp > 0:
        count += 1
        temp = temp // 10

    temp = n
    while temp > 0:
        d = temp % 10
        sum = sum + (d ** count)
        temp = temp // 10

    if sum == n:
        print(n, "is an Armstrong number")