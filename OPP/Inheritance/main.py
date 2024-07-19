from Car import Car # * Importing the Car 
from Vehicle import Vehicle # * Importing the Vehicle 

def main() :
    
    car = Car("Honda", "Civic") #* Subclass
    car.go()
    car.stop()
    
    vehicle = Vehicle("Carbon", "Civic") # * superclass 
    vehicle.go()
    vehicle.stop()

main()