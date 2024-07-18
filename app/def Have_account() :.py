def Have_account() :

    while True : # * loop for user 

        do_have_account = input("Do you have account? [y/N]: ") # * Do you have account? 

        if do_have_account == "N" or do_have_account == "n" :
            pass # ! Create a email&password  
        elif do_have_account == "y" or do_have_account == "Y" :
            break 
        
    return do_have_account 
