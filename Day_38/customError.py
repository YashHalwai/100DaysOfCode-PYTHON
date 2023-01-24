# Raising custom errors in Python | Python Tutorial - Day #38

# https://www.youtube.com/watch?v=Phr4CNppYoM&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=38



a = input("Enter the value between 5 and 9: ")

if(a == "quit"):
    print("Okay")

elif(int(a) < 5 or int(a) > 9):
    raise ValueError("Value should be between 5 and 9")