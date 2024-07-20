
# ? 4 OOP Pillars
# * Inheritance  
# * Abstract 
# * Polymorphism
# * Encapsulation 


# Todo create a simple Inheritance 

class Person:
    
    #* This is the Superclass
    
    def __init__(self,name,age) :
        self.name = name 
        self.age = age 
    
    def get_name(self) :
        pass 
    
    def get_age(self) :
        pass

class Niyari(Person) : 
    
    #* This is the subclass inherit the superclass(Person)

    def __init__(self, name, age, gender) :
        super().__init__(name, age) 
        self.gender = gender
    
    
    # * Creating a method 
    
    def get_name(self) :
        print(f"Hello {self.name} desu! ")
    
    def age(self) :
        print(f"Age is {self.age}")
    
    def gender(self) :
        print(f"I'm a {self.gender}")



def main() :
    
    niyari = Niyari("Niyari", 19, "Female")
    
    niyari.name()
    niyari.age()
    niyaru.gender()

main()