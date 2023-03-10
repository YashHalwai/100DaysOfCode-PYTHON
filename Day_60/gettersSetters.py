# Getters and Setters in Python | Python Tutorial - Day #60

# https://www.youtube.com/watch?v=2gbCT8h9uyk&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=60

class MyClass:
    
    def __init__(self,value):
        self.value = value
        
    def show(self):
        print(f"Value is {self._value}")
        
    @property
    def ten_value(self):
        return 10 * self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10
    
    
obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()