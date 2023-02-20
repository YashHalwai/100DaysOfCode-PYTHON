# Lambda functions in Python | Python Tutorial - Day #52

# https://www.youtube.com/watch?v=UfFWf-PXUqE&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=52


# Anonymous Function

# def double(x):
#     return x*2


def appl(fx, value):
    return 6 + fx(value) 


double = lambda x : x * 2
cube = lambda x : x * x *x
avg = lambda x,y,z : (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(5,5,10))

print(appl(lambda x : x * x * x, 2))