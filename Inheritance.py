
# * Inheritance 

class main :

    # * Parent Class
    def __init__(self) :
        pass 

    def Vehicle(self) :
        self.go() ;
        self.stop() ;

    def go(self) :
        print("This Vehicle is moving")
    
    def stop(self) :
        print("This Vehicle is stopped")

class Car(main) :

    # * Subclass 




