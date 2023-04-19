# AsyncIO in Python | Python Tutorial - Day #96

# https://www.youtube.com/watch?v=lgoB3_-ejnI&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=96


import time 
import asyncio


# def fun1():
    
#     time.sleep(3)
#     print("fun 1")

# def fun2():
    
#     time.sleep(3)
#     print("fun 2")    
    
# def fun3():
    
#     time.sleep(3)
#     print("fun 3")      
    
# fun1()    
# fun2()
# fun3()


async def fun1():
    
    await asyncio.sleep(3)
    print("fun 1")

async def fun2():
    
    await asyncio.sleep(2)
    print("fun 2")    
    
async def fun3():
    
    await asyncio.sleep(4)
    print("fun 3")
    
# async def main():
#     task = asyncio.create_task(fun1())          
#     await fun2()
#     await fun3()


async def main():
    
    L = await asyncio.gather(fun1(),fun2(),fun3())

asyncio.run(main())