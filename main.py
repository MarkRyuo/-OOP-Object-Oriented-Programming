
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

# for_Loop() 

def while_loop() :

    while True :

        num1 = input("Enter a number: ") 
        num2 = input("Enter a number: ")

        if num1.isdigit() and num2.isdigit() :
            num1 = int(num1)
            num2 = int(num2)
            total_of = num1 + num2 
            print(total_of)
        else :
            print(f"{num1}, {num2} is not a number")
    
# while_loop() 


# * Class 

class Animal() :

    def __init__(self, name_of_animal, age_of_animal):
        self.name_of_animal = name_of_animal 
        self.age_of_animal = age_of_animal 
    
    def Dog(self):
        
        while True :

            name_of_Dog = input("Enter name of Dog: ") 
            age_of_Dog = input("Enter age of your Dog: ")

            if name_of_Dog :
                print()
            else:
                print(f"Your dogs name is {name_of_Dog}.")
            
        
        
        


