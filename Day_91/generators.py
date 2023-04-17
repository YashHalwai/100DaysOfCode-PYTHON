# Generators in Python | Python Tutorial - Day #91

# https://www.youtube.com/watch?v=ixd-u3pmsUc&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=91


def my_generator():
    
    for i in range(5):
        
        yield i
        
gen = my_generator()        

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    
    print(j)