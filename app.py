
# * Create a userLog 




def Have_account() :

    while True : # * loop for user 

        do_have_account = input("Do you have account? [y/N]: ") # * Do you have account? 

        if do_have_account == "N" or do_have_account == "n" :
            pass # ! Create a email&password  
        elif do_have_account == "y" or do_have_account == "Y" :
            break 
        
    return do_have_account 



def Log_in() : # * This block code is for log in only 

    def _username() :
        
        while True :
            
            get_username = input("Enter your username: ")
            
            if get_username.isdigit() : # * isdigit check for all of get_username is a digit number 
            if get_username :
                print("Invalid username the content is number")
        else : 
            break 

        return get_username
    
    _username()




def main() :

    Have_account()
    Log_in()




main()