users = {"user1": "qwerty12!!",
"user2": "asdfgh44",
"user3": "hellopeople",
"user4": "conrad12",
"user5": "jeremiah433&"}


entered_userName = input("Enter your username: ")
entered_password = input("Enter your password: ")

for user, password in users.items():
    if entered_userName not in users:
        print("Invalid user")
        break
    if users[entered_userName] != entered_password:
        print("Invalid user")
        break
    else:
        print("Valid user! Logged In")
        break



