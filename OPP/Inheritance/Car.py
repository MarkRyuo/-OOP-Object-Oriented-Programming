from Vehicle import Vehicle 

class Car(Vehicle) :
    
    def __init__(self, name, types):
        super(self, name, types)
    
    def go(self):
        print("The car is go!")
    
    def stop(self):
        print("The car is stopped!")


