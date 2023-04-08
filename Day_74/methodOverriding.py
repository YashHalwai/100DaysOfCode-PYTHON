# Method Overriding in Python | Python Tutorial - Day #74

# https://www.youtube.com/watch?v=46_yfYC36JY&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=74

class Shape:
    
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        
    def area(self):
        return self.x * self.y

class Circle(Shape):
        
    def __init__(self,x):
        
        self.x = x
        
    def area(self):
        return 3.14 * self.x * self.x
    
# rec = Shape(3,5)
# print(rec.area())    

# cir = Circle(5)
# print(cir.area())    


c = Circle(5)
print(c.area())