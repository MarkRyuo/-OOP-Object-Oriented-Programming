
# Todo Create a user log Only 


class main :

    def __init__(self) :
        pass

    
    def User(self) :
        self.username()
        self.user_password()
    
    def username(self) :

        while True :

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


class Username(main) :


    def welcoming(self) :
        print(f"Welcome user {username}")






def main() :

    User = Username()
    User.username()

    if User :
        User.welcoming()
    else:
        pass
    


main()