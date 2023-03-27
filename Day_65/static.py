# Static Methods in Python | Python Tutorial - Day #65

# https://www.youtube.com/watch?v=GcSVYNSsJxo&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=65

class Math:
    
    def __init__(self,num):
        self.num = num
        
    def addtonum(self,n):
        self.num = self.num + n
        
    @staticmethod
    def add(a, b):
        return a + b
    
# result = Math.add(1,2)
# print(result)        

a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7,2))