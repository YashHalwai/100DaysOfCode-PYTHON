# Exercise 7 Solution + Shoutouts | Python Tutorial - Day #75

# https://www.youtube.com/watch?v=Wt9Shnzv_Yg&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=75

import os

# os.rename("clutteredFolder/file.txt", "clutteredFolder/6.txt")

files = os.listdir("Day_75/clutteredFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"Day_75/clutteredFolder/{file}",f"Day_75/clutteredFolder/{i}.png")
        i = i + 1
        
        