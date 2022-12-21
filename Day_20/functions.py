# Functions in Python | Python Tutorial - Day #20

# https://www.youtube.com/watch?v=dyvxxJSGUsE

def calculateGmean(a,b):
    mean = (a * b) / (a + b)
    print(mean)
    
def isGreater(a,b):
    if( a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")   

def isLesser(a,b):
    pass

a = 9
b = 8
  
# gmean1 = (a * b) / (a + b) 
# print (gmean1)

calculateGmean(a, b)
isGreater(a,b)

c = 8
d = 7

calculateGmean(c,d)
isGreater(c,d)

# gmean2 = (c * d) / (c + d)
# print(gmean2)