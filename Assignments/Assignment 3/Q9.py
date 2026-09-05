# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = float(input("Enter marks of subject 1: "))
sub2 = float(input("Enter marks of subject 2: "))
sub3 = float(input("Enter marks of subject 3: "))
sub4 = float(input("Enter marks of subject 4: "))
sub5 = float(input("Enter marks of subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
print(f'Total : {total}')
percentage = total / 5
print(f'Percentage : {percentage}')

if percentage >= 60:
    print("First Class")
elif percentage >= 50:
    print("Second Class")
elif percentage >= 40:
    print("Third Class")
else:
    print("Fail")