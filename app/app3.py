
# Todo Create a user log using Inheritance 

class main : # * Declaring Parent or Superclass

    def __init__(self) :  # * Declaring Constructor 
        pass

    
    def User(self) : # ! Declaring Constructor in a Method 
        self.username()
        self.user_password()
    
    def username(self) :
        pass # *

    
    def user_password(self) :
        pass


class Username(main): # * Conrete ``

    def username(self) : # ! Method? 

        while True : # * Loop 

            username = input("Enter your username: ") 

            if username.isdigit() :
                if username :
                    print(f"Unsupported username, Try Again!")
            else :
                print(f"Loading Username......")
                break

        return username
    
    def user_password(self):

        user_attempt = 2 # * User attempt declare limit 2  
        user_pass = True # * user_password boolean

        while user_pass:

            user_password = input("Enter your password: ")

            if user_password.isdigit() :
                user_attempt -= 1 
                print("Unsupported password, Try Again!")
            else :
                print("Loading Password.......")  #* If password is true not digits number
                user_pass = False 

            if user_attempt == 0 : #* Logic for attempting password 
                print("2 Attempt Block 🔐")
                break

        return user_password




def main() :

    User = Username() # * Call the subclass Username
    print(f"Welcome user: {User.username()}")
    print(f"Password : {User.user_password()}")



main() 

