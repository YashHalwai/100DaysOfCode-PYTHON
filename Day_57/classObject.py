# Classes and Objects in Python | Python Tutorial - Day #57

# https://www.youtube.com/watch?v=a7baAGCBA9U&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=57


class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nikita"
b.occupation = "HR"

c.name = "Yash"
c.occupation = "Data Scientist"

a.info()
b.info()
c.info()