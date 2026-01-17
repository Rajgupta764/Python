print("creat your account")
name=input("Enter your name:")
password=input("Enter your password:")
print("Your account has been created successfully")

print("Login here:")
lname=input("Enter username:")
lpassword=input("Enter your password:")


if name==lname and password==lpassword:
    print("Login successfully")
else:
    print("Invalid username of password")
    