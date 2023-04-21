# Multithreading in Python | Python Tutorial - Day #97

# https://www.youtube.com/watch?v=ICbU6zAKtqQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=97


import threading
import time


# Indicates some task being done


def func(seconds):
    
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# func(4)    
# func(2)
# func(1)

# Same code using threads


# time1 = time.perf_counter()

# t1 = threading.Thread(target=func,args=[4])
# t2 = threading.Thread(target=func,args=[2])
# t3 = threading.Thread(target=func,args=[1])

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# time2 = time.perf_counter()
# print(time2 - time1)


def poolingDemo():
    
    with ThreadPoolExecutor() as executor:
        
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 2)
        print(future2.result())
        future3 = executor.submit(func, 4)
        print(future1.result())
        print(future3.result())

poolingDemo()        