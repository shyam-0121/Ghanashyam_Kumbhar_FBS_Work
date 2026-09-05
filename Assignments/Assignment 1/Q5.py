# Calculate Compound Interest
P = int(input("Enter Principal :"))
R = int(input("Enter Rate of Interest: "))
T = int(input("Enter Years: "))

CI = P * (1 + R / 100) ** T - P

print(f'Compound Interest: {CI}')