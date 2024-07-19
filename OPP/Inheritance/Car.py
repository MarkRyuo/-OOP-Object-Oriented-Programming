from Vehicle import Vehicle 

class Car(Vehicle) :
    
    def __init__(self, name, types):
        super().__init__(name, types)
    
    def go(self):
        print(f"The car is go!, {self.name}")
    
    def stop(self):
        print(f"The car is stopped!, {self.types}")


