
# * Variable 

username = "Jhon Mark" # * String/ str 
age = 21 #* Integer / Int 
Online = True # * Boolean / Bool 
gpa= 1.50 # * Float 
password = "JM01" # * Complex 

# * Operators - Addition +, Multiplication  *, Subtraction -, Division /, Modulus %, Exponentiation 
# *          ** 
# *          // 


#* LOOP'S  - While Loop & for loop 


# * CONDITION  - If / else / elif statement 

# * Function - def(define)


def while_loop() :

    username = input("Enter your name: ")
    
    while True :

        if username :
            if username == "Jhon Mark" :
                print(f"Hello {username}") # * 'f' String 
                break
        else :
            print(f"LOL {username}")
            break



# while_loop() 


# * LIst, Dict, Set, Tuple 

this_is_List = ["List0", "List1", "List2", "List3"] # * List is Changeable

this_is_Dict = {
    "Name" : "Jhon Mark",
    "Age" : 21,
    "Online" : True,
    "Gpa" : 1.0,
    "Password" : "Jm21"
}

this_is_Tuple = ( # * Tuple is not Changeable 
    "List0", 
    "List1",
    "List2",
    "List3"
) 

# * Append(), Remove(), Clear(), Insert() - List, Dict 