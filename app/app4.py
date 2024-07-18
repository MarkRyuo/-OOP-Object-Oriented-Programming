

# * Create a Calculator using OOP 



class Calculator :
    # * Parent class

    def __init__(self) :
        pass 
    
    def Calculator(self) : # * Constructor 
        self.addition()
        self.multiplication()
        self.division()
        self.subtraction()

    def addition(self) :
        pass
    
    def multiplacation(self) :
        pass

    def division(self) :
        pass

    def subtractio(self) :
        pass


class Addition(Calculator) : # * Child class 

    def add_this(self) : # * Method 

        while True :

            addA = input("Enter a number A: ")
            addB = input("Enter a number B: ")

            if addA and addB :
                return addA + addB
                break 
            else :
                return false 
            
        return addA, addB
    






def main() : # * Main function to run 

    add = Addition()
    add.add_this()

    


main()













































