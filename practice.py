correct_username = "Anchal"
correct_password = 12345
attempt = 0
while attempt<3:
    username = input("Enter the username: ")
    password = input("Please enter your password: ")
    if username ==correct_username or password ==correct_password:
        print("you are successfully log in:")
        break
    else:
        attempt+=1
        if attempt<3:
            print("wrong username or password try again!")
else:
    print(" too many wrong attempts login faild!")
