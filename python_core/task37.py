from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass
    def calculatePerimeter(self):
        pass

class circle(Shape):
    def calculateArea(self,r):
        print(f"area is: {3.14*r*r}")
        return super().calculateArea() 
    def calculatePerimeter(self,r):
        print(f"perimeter is: {3.14*r*2}")
        return super().calculatePerimeter()  

class triangle(Shape):
    def calculateArea(self,b,h):
        print(f"area is: {0.5*b*h}")
        return super().calculateArea() 
    def calculatePerimeter(self,a,b,c):
        print(f" is:perimeter {a+b+c}")
        return super().calculatePerimeter()      

c=circle()
t=triangle()
c.calculateArea(2)
c.calculatePerimeter(3)
t.calculateArea(2,4)
t.calculatePerimeter(3,4,2)    