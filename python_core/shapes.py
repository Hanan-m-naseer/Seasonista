from abc import ABC, abstractmethod
class shapes(ABC):
    @abstractmethod
    def calculateArea(self):
        pass

class circle(shapes):
    def calculateArea(self,r):
        print("Area of circlie is: ")
        print(3.14*r*r)
        return super().calculateArea()
    
class rectangle(shapes):
    def calculateArea(self,l,b):
        print("Area of rectangle is: ")
        print(l*b)
        return super().calculateArea()    
c = circle()
rect = rectangle()
c.calculateArea(2)
rect.calculateArea(2,4)