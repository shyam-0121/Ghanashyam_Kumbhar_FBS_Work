# Write a program to prompt user to enter userid and password. If Id and 
# password is incorrect give him chance to re-enter the credentials. Let him 
# try 3 times. After that program should terminate.

correct_userid = "admin"
correct_password = "12345"

for i in range(3):
    userid = input("Enter userid: ")
    password = input("Enter password: ")

    if userid == correct_userid and password == correct_password:
        print("Login successful")
        break
    else:
        print("Invalid userid or password")
else:
    print("You have exceeded the maximum number of attempts. Program terminated.")