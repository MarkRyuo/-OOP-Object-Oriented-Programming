
# Todo Create a user log Only 


class main :

    def __init__(self) :
        pass

    
    def User(self) : # ! Abstract?
        self.username()
        self.user_password()
    
    def username(self) : # ! Method? 

        while True : # * Loop 

            username = input("Enter your username: ") 

            if username.isdigit() :
                if username :
                    print(f"Unsupported username, Try Again!")
            else :
                print(f"Loading.....")
                break

        return username

    
    def user_password(self) :
        pass


class Username(main): # * Conrete

    def welcoming(self) :
        print(f"Welcome user {username()}")




def main() :

    User = Username() # * Call the subclass Username
    User.username()

    if User :
        User.welcoming()
    else:
        pass
    


# main() 

User = Username() # * Call the subclass Username
User.username()

User.welcoming()