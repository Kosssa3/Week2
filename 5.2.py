correct_password = "Zdejmito1234"

password = input("Enter password: ")
while password != correct_password:
    print("Incorrect password. Try again.")
    password = input("Enter password: ")
print("Welcome!")
