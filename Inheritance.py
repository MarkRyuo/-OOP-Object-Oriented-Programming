
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

#* Car function is the Descendance of the Main
class Car(main) : # * For java we need extend to Inherit the parent. In python this is how it works 

    # * Sub-class 

    def wheels(self): # * Method 
        return 4
    
    def doors(self) :
        return 4


class Bicycle(main) :
    
    #* Sub-class 

    def wheels(self) :
        return 2
    
    def pedals(self) :
        return 2


car = Car()
car.go()
print(f"The car have {car.wheels()} wheels")
car.stop()
print()
bike = Bicycle()
bike.go()
print(f"The bicycle have {bike.wheels()} wheels")
bike.stop()





