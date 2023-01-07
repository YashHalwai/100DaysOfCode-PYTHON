# Exercise 2: Solution & Shoutouts | Python Tutorial - Day #26

# https://www.youtube.com/watch?v=IZBKXWrbqBM&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=26

import time
name = input("Enter your name: ").title()    

hour = int(time.strftime('%H'))

if 4 <= hour< 12:
    print("Good Morning", name)
elif 12 <= hour < 17:
    print("Good Afternoon", name)
elif 17 <= hour < 21:
    print("Good Evening", name)        
else:
    print("Good Night", name)    