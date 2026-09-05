# Find the percentage of 5 subjects marks
M1 = int(input("Enter Marks of Java:"))
M2 = int(input("Enter Marks of C++:"))
M3 = int(input("Enter Marks of C:"))
M4 = int(input("Enter Marks of JS:"))
M5 = int(input("Enter Marks of Python:"))

# Calculate Total Marks
Total = M1 + M2 + M3 + M4 + M5

# Percentage 
Percentage = Total / 5

print(f"Total Marks:{Total}")
print(f'Percentage :{Percentage}')