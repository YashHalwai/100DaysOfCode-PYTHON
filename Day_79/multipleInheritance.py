# Multiple Inheritance in Python | Python Tutorial - Day #79

# https://www.youtube.com/watch?v=4o7xSHgKlvI&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=79


class Employee:
    
    def __init__(self,name):
        
        self.name = name
        
    def show(self):
        
        print(f"The name is {self.name}")    
        
class Dancer:
    
    def __init__(self,dance):
        
        self.dance = dance
    
    def show(self):
        
        print(f"The dance is {self.dance}")    
        
class DancerEmployee(Employee, Dancer):
    
    def __init__(self,dance,name):
        
        self.dance = dance
        self.name = name
        

o = DancerEmployee("Kathak","Shivani")                        
print(o.name)
print(o.dance)
o.show()

print(DancerEmployee.mro())