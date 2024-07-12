
# Todo Create a user log using Inheritance 

class main :

    def __init__(self) :
        pass

    
    def User(self) : # ! Abstract?
        self.username()
        self.user_password()
    
    def username(self) :
        pass

    
    def user_password(self) :
        pass


class Username(main): # * Conrete

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
    
    def user_password(self):

        user_attempt = 2 # * User attempt limit 2  

        while True:

            user_password = input("Enter your password: ")

            if user_password




def main() :

    User = Username() # * Call the subclass Username
    print(f"Welcome user: {User.username()}")
    


main() 

