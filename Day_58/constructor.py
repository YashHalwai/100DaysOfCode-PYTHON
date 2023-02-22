# Constructors in Python | Python Tutorial - Day #58

# https://www.youtube.com/watch?v=12HRkYld22c&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=58


class Person:
    
    def __init__(self,name,occ):
        print("Hey I am a person")
        self.name = name
        self.occ = occ
        
    def info(self):
        print(f"{self.name} is a {self.occ}")    

    
a = Person("Harry", "DS")        
b = Person("Divya", "HR")
a.info()
b.info()