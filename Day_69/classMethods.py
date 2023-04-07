# Class Methods in Python | Python Tutorial - Day #69

# https://www.youtube.com/watch?v=9ynmDLc5FYo&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=69

class Employee:
    
    company = "Apple"

    def show(self):
        
        print(f"The name is {self.name} and company is {self.company}.")
    
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany
        
e1 = Employee()            
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)