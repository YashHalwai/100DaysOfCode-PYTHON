# Hybrid and Hierarchical Inheritance in Python | Python Tutorial - Day #81

# youtube.com/watch?v=B4Q8zxRkm_I&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=81


# Example of Hybrid Inheritance

class BaseClass:
    
    pass

class Derived1(BaseClass):
    
    pass

class Derived2(BaseClass):
    
    pass

class Derived3(Derived1, Derived2):
    
    pass


# Hierarchical Inheritance


class BaseClass:
    
    pass

class D1(BaseClass):
    
    pass

class D2(BaseClass):
    
    pass

class D3(D1):
    
    pass