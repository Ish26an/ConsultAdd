print("Enter username and password")
count = 0
while count < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if password == "ishan26" and username == "Ishan":
        print("Access Granted.")
        break
    else:
        print("Access denied")
        count += 1

