# Inheritance in Python | Python Tutorial - Day #61

# https://www.youtube.com/watch?v=-KsfUaQEY9Y&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=61

class Employee:
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def showDetails(self):
        print(f"The name of employee: {self.id} is {self.name}")
        
class Programmer(Employee):
    
    def showLanguage(self):
        print("The default language is Python")
        
e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()        