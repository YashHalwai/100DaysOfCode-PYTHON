# Function Caching in Python | Python Tutorial - Day #92

# https://www.youtube.com/watch?v=K8gjSwc3Rlo&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=92


from functools import lru_cache
import time


@lru_cache(maxsize=None)

def fx(n):
    
    time.sleep(5)
    return n*5


print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
print(fx(6))
print("Done for 6")