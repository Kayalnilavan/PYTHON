username="YarlIT"
password="Yit2009"

u_name = input("Username : ")
pswd = input("Password : ")
role=input("Role : Admin/User\nRole :")

if username==u_name and password==pswd :
    print("Login success")
    
    if role=="Admin" :
        print("Welcome to Admin Dashboard")
    elif role=="User" :
        print("Welcome to User Dashboard")
    else : 
        print("Invalid role")
else :
    print("Invalid username or password")