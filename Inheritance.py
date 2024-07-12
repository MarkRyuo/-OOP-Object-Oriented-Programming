
# * Inheritance 

class main :

    # * Parent Class
    def __init__(self) :
        pass 

    def Vehicle(self) :
        self.go() ;
        self.stop() ;

    def go(self) :
        print("This Vehicle is moving!")
    
    def stop(self) :
        print("This Vehicle is stopped!")

class Car(main) :

    # * Subclass 

    def wheels(self):
        wheels = 4
        return wheels


class Bicycle(main) :
    
    #* Subclass 

    wheels = 2
    pedals = 2 


car = main(), Car()
car.go()
print(f"The car have {car.wheels} wheels")





