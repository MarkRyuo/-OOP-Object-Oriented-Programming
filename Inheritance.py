
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

    # * Sub-class 

    def Wheels(self):
        return 4


class Bicycle(main) :
    
    #* Sub-class 

    wheels = 2
    pedals = 2 


car = Car()
car.go()
print(f"The car have {car.Wheels()} wheels")





