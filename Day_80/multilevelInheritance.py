# Multilevel Inheritance in Python | Python Tutorial - Day #80

# https://www.youtube.com/watch?v=Il7XMJJeXiA&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=80


class Animal:
    
    def __init__(self,name,species):
        
        self.name = name
        self.species = species
        
    def show_details(self):
        
        print(f"Name : {self.name}")    
        print(f"Species: {self.species}")


class Dog(Animal):
    
    def __init__(self,name, breed):
        
        Animal.__init__(self,name,species="Dog")        
        self.breed = breed
        
    def show_details(self):
        
        Animal.show_details(self)  
        print(f"Breed: {self.breed}")  
        

class GoldenRetriever(Dog):
    
    def __init__(self,name,color):
        
        Dog.__init__(self,name,breed = "Golden Retriever")        
        self.color = color
        
    def show_details(self):
         Dog.show_details(self)
         print(f"Color : {self.color}")
            

o = GoldenRetriever("Tommy", "Black")       
# o = Dog("Tommy", "Black")   
# o = Animal("Tommy", "Black")      
# print(o)

o.show_details()

# print(GoldenRetriever.mro())