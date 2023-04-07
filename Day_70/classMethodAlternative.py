# Class Methods as Alternative Constructors in Python | Python Tutorial - Day #70

# https://www.youtube.com/watch?v=FGlKJdy--p8&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=70

class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = 12000

    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)

string = "Harry-12000"
e2 = Employee(string.split("-")[0],string.split("-")[1])
print(e2.name)
print(e2.salary)