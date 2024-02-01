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
            f.write((user_name := input("Enter the username : ").lower()) + " : "+ (pwd := input("Enter password : ").lower()) + "\n")
            print("Password succesfullt added to the application")
        
        else:
            print("Wrong password, try again!")
            main()

# used to retrieve the passwords from the application
def ret_pwd():
    
    with open('password.txt', 'r') as f:

        if f.read() == " ":
            print("There are no entries in the application")

        for entry in f.readlines():
            if (user_name := input("Enter the username : ").lower()) == entry:
                return entry
            
        return "There is no such username. Try again"

# driver code
def main():
    print("Do you want to add or retrieve the passwords ? ")
    user_input = input("(ret/add): ").lower()

    if user_input == "ret":
        ret_pwd()
    elif user_input == "add":
        add_pwd()
if _name_ == "_main_":
    main()
