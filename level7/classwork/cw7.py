

registered_password = "Password123"

while True:
    user_input = input("Enter your password")
    if user_input == registered_password:
        print("Welcome!")
        break
    else:
        print("Incorrect")


#registered_password = "luka123."
# entered_password = ""

# while entered_password != registered_password:
#     entered_password = input("Please enter password: ")

#     if entered_password != registered_password:
#         print("Please input correct password")
#     else:
#         print("Access granted")

registered_password = "luka123."
entered_password = ""
attempts = 0  

while entered_password != registered_password and attempts < 3:
    entered_password = input("Please enter password: ")
    attempts += 1

    if entered_password != registered_password:
        if attempts < 3:
            print("Incorrect password, try again.")
        else:
            print("Too many failed attempts. Access denied.")
    else:
        print("Access granted.")

 