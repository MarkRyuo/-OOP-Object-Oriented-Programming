
# * Variable 

username = "Jhon Mark" # * String/ str 
age = 21 #* Integer / Int 
Online = True # * Boolean / Bool 
gpa= 1.50 # * Float 
password = "JM01" # * Complex 

# * Operators - Addition +, Multiplication  *, Subtraction -, Division /, Modulus %, Exponentiation **, Floor Division //

#* LOOP'S  - While Loop & for loop 

# * CONDITION  - If / else / elif statement 

# * Function - def stands for Define 

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



def for_Loop() :

    Empty_List = [] 

    for i in range(1, 10) :
        Empty_List.append(i) # * Understanding the Append - Empty_List i-append yung i 
    print(Empty_List)

for_Loop()

def while_loop() :

    while True :

        num1 = input("Enter a number: ") 
        num2 = input("Enter a number: ")

        if num1.isdigit && num2.isdigit :
            print(num1 + num2) 
        else :
            print(ff"")