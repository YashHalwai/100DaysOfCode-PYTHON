# super keyword in Python | Python Tutorial - Day #72

# https://www.youtube.com/watch?v=P648reefNh0&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=72


class Employee:
    
    def __init__(self, name, id):
        
        self.name = name
        self.id = id

class Programmer(Employee):
    
    def __init__(self,name,id,lang):
        
        super().__init__(name,id)
        self.lang = lang
        
rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")

print(harry.name)
print(harry.id)
print(harry.lang)