from Car import Car 
from Vehicle import Vehicle 

def main() :
    
    car = Car("Honda", "Civic")
    car.go()
    car.stop()
    
    vehicle = Vehicle("Carbon", "Civic")
    vehicle.go()
    vehicle.stop()

main()