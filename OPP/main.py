
# ? 4 OOP Pillars
# * Inheritance  
# * Abstract 
# * Polymorphism
# * Encapsulation 


# Todo create a simple Inheritance 

class Person() :
    
    #* This is the Superclass
    
    def __init__(self,name,age) :
        self.name = name 
        self.age = age 
    
    def name(self) :
        pass 
    
    def age(self) :
        pass

class Niyari(Person) : 
    
    #* This is the subclass inherit the superclass(Person)

    def __init__(self, name,age,gender) :
        super.__init__(name,age) 
        self.gender = gender 
    
    
    # * Creating a method 
        
