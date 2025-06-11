from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Lion(Animal):
    def sound(self):
        print("this is lion roaring")
        return super().sound()   

class Tiger(Animal):
    def sound(self):
        print("this is tiger roaring")
        return super().sound()            
    
l = Lion()
t = Tiger()
l.sound()
t.sound()