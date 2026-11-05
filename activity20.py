from getpass import getpass

isLogin = False

while isLogin == False:
    username = input("Input username: ")
    password = input("Input password: ")

    if username == "Daniepot" and password == "imissyou123":
        print("Access Granted")
        isLogin = True
    else:
        print("Access Denied")
        isLogin = False