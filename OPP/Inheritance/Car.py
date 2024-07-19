from Vehicle import Vehicle 

class Car(Vehicle) :
    
    def __init__(self, go, stop):
        super(self, go, stop)
    
    def go(self):
        print("The car is go!")
    
    def stop(self):
        print("The car is stopped")