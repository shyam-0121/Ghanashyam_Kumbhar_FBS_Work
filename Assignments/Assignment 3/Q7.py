# Write a program to check if user has entered correct userid and password.

correct_userid = "admin"
correct_password = "12345"

userid = input("Enter userid: ")
password = input("Enter password: ")

if userid == correct_userid and password == correct_password:
    print("Login successful")
else:
    print("Invalid userid or password")