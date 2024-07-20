from abc import ABC, abstractmethod


# * Superclass || Parent class 

class Pets(ABC):
    
    @abstractmethod
    
    def speak(self) :
        print("This is Pets")
    