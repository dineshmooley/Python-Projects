print("Welcome to Password Manager")

# used to verify user of the application
def valid_user() -> bool:
    app_pwd = "kumar"
    ver = input("Enter application password : ")
    if ver == app_pwd:
        return True

    return False

# used to add new passwords to the application
def add_pwd():
    with open('password.txt','a') as f:
        if valid_user():
            f.write((user_name := input("Enter the username : ").lower()) + ":"+ (pwd := input("Enter password : ").lower()) + "\n")
            print("Password succesfully added to the application")
            main()
        
        else:
            print("Wrong password, try again!")
            main()

# used to retrieve the passwords from the application
def ret_pwd():
    
    with open('password.txt', 'r') as f:

        if valid_user():
            found = False
            user_inp = input("Enter the username : ")
            for entry in f.readlines():
                username, password = entry.rstrip().split(":")
                if user_inp == username:
                    print("Password is : ",password)  
                    found = True                     

            if not found:
                print("No such username")
                main()
        else:
            print("Wrong password, try again!")
            main()

        

# driver code
def main():
    print("Do you want to add or retrieve the passwords ? ")
    user_input = input("(ret/add): ").lower()

    if user_input == "ret":
        ret_pwd()
    elif user_input == "add":
        add_pwd()

if __name__ == "__main__":
    main()
