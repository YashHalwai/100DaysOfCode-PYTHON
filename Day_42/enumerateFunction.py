# Enumerate Function in Python | Python Tutorial - Day #42

# https://www.youtube.com/watch?v=kGnYc_h1geM&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=42

# enumerate => inbuilt function

marks = [4, 5, 7, 6, 5, 45, 10, 53]

for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 3):
        print("Harry, awesome!")