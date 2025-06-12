class Rectangle:
    def __init__(self,length,breadth):
        self.length,self.breadth = length,breadth
    
    def area(self):
        print(f"Area of rectangle is :",self.length * self.breadth)
    
    def perimeter(self):
        print(f"Perimeter of rectangle is :",2*(self.length+self.breadth))

rec = Rectangle(20,30)
rec.area()
rec.perimeter()