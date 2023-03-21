# Access Modifiers in Python | Python Tutorial - Day #62

# https://www.youtube.com/watch?v=43FK20rWvKQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=62

class Student:
    
    def __init__(self):
        self._name = "Harry"
        
    def _funname(self):  # protected method
        return "CodeWithHarry"
    

class Subject(Student): # inherited class
    pass

obj = Student()        
obj1 = Subject()

# calling by object of Student Class
print(obj._name)
print(obj._funname())

# calling of object of Student Class
print(obj1._name)
print(obj1._funname())