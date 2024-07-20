
# * Create a simple inheritance
# * Vehicle is the superclass and the Car is the subclass  

class Vehicle :
    
    #* Superclass
    
    def __init__(self, name, types) :
        self.name = name 
        self.types = types
    
    def go(self): # * Method 
        print("superclass go ") 
    
    
    def stop(self) :
        print("superclass stop")
    
    