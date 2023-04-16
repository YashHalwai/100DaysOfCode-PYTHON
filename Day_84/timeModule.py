# Time Module in Python | Python Tutorial - Day #84

# https://www.youtube.com/watch?v=oTtIvV-Q1FY&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=84


import time
# print(time.time())


# print(4)
# time.sleep(3)
# print("This is printed after 3 seconds")


t = time.localtime()
formatted_time = time.strftime("%Y - %m - %d %H : %M : %S", t)
print(formatted_time)