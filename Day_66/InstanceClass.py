# Instance variables vs Class variables in Python | Python Tutorial - Day #66

# https://www.youtube.com/watch?v=tQdaeiF4j38&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=66

class Employee:
    
    company_name = "Apple"
    noOfEmployees = 0
    
    def __init__(self,name):
        
        self.name = name
        self.raise_amount = 0.02
        
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.company_name} is {self.raise_amount}")    


# Employee.showDetails(emp1)

emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.company_name = "Apple"
Employee.noOfEmployees += 1
emp1.showDetails()


emp2 = Employee("Rohan")
emp2.company_name = "Nestle"
emp2.showDetails()