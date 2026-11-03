correct_username = "admin"
correct_password = "python123"

login = input("Put correct username: ")
password = input("Put correct password: ")
if login == correct_username and password == correct_password:
    print("Access granted!")
elif login != correct_username or password != correct_password:
    print("Access denied!")
