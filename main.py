
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

    def __init__(self) -> None:
        pass
    
    def Dog(self):


        def Name_Of_Dog() :

            while True :

                name_of_Dog = input("Enter name of Dog: ") 

                if name_of_Dog.isdigit():
                    print(f"Dog is not found!, Try Again! ")
                else:
                    print(f"Your dogs name is {name_of_Dog}.")
                    break
                
            return name_of_Dog
            
        Name_Of_Dog()


        def Age_Of_Dog() :

            while True :
                
                age_of_Dog = input("Enter age of your Dog: ")
                
                if age_of_Dog.isdigit() :
                    print(f"Your dog age is {age_of_Dog}")
                    break
                else :
                    print(f"{age_of_Dog} is not a number, Try Again! ")

            return age_of_Dog
        
        Age_Of_Dog()
    
    def Cat(self) :

        def name_of_Cat() :

            name_Cat = True 

            while name_Cat :

                NAME_OF_CAT = input("Enter Name of your cat: ")

                if NAME_OF_CAT.isdigit() :
                    print(f"Cat name is not a Number")
                else :
                    print(f"Your cat name is {NAME_OF_CAT}")
                    name_Cat = False

            return NAME_OF_CAT

        name_of_Cat()
            
        


animal = Animal() 
# animal.Dog()


animal.Cat()













