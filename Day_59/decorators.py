# Decorators in Python | Python Tutorial - Day #59

# https://www.youtube.com/watch?v=PTBZ674EsvI&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=59&t=1s

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")    
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World")

@greet
def add(a,b):
    print(a+b)        
    
hello() 
add(5,5)   