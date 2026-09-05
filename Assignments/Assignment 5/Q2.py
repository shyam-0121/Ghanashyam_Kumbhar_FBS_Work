# Enter number of students from user. For those many students accept marks of 
# 5 subject marks from user and calculate percentage. Display all percentage and 
# average percentage of students.

n = int(input("Enter number of students: "))
total_percentage = 0

for i in range(n):
    print(f"Enter marks of student {i+1}:")
    sub1 = float(input("Subject 1: "))
    sub2 = float(input("Subject 2: "))
    sub3 = float(input("Subject 3: "))
    sub4 = float(input("Subject 4: "))
    sub5 = float(input("Subject 5: "))

    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5
    print(f"Percentage of student {i+1}: {percentage}")

    total_percentage += percentage

average_percentage = total_percentage / n
print("Average percentage of all students:", average_percentage)