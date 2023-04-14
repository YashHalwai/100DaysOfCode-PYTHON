# Single Inheritance in Python | Python Tutorial - Day #78

# https://www.youtube.com/watch?v=U53_Gw55NI8&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=78

class Animal:
    
    def __init__(self, name, species):
        
        self.name = name
        self.species = species
        
    def make_sound(self):
        
        print("Sound made by the animal")    


class Dog(Animal):
    
    def __init__(self,name,breed):
        
        Animal.__init__(self,name,species = "Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")    
        

class Cat(Animal):
    
    def __init__(self,name,breed):
        
        Animal.__init__(self,name,species = "Cat")
        self.breed = breed
        
    def make_sound(self):
        print("Meow!")         
        
# d = Dog("Dog", "Lab")        
# d.make_sound()

d = Cat("Cat", "Tom")        
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()