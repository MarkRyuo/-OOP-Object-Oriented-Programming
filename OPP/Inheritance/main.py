from Car import Car 
from Vehicle import Vehicle 

def main() :
    
    car = Car("Honda", "Civic") #* Subclass
    car.go()
    car.stop()
    
    vehicle = Vehicle("Carbon", "Civic") # * superclass 
    vehicle.go()
    vehicle.stop()

main()