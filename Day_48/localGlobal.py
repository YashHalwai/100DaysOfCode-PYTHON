# Local vs Global Variables in Python| Python Tutorial - Day #48

# https://www.youtube.com/watch?v=RaG6GgcDt54&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=48

x = 10


def my_function():
    
    global x # global variable
    
    x = 5
    y = 5 # local variable
    
my_function()
print(x)    
# print(y) 