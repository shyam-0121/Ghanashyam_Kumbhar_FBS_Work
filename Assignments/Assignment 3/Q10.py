# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if gender.lower() == "male":
    if age >= 21:
        print("Eligible to marry")
    else:
        print("Not eligible to marry")
elif gender.lower() == "female":
    if age >= 18:
        print("Eligible to marry")
    else:
        print("Not eligible to marry")
else:
    print("Invalid gender")