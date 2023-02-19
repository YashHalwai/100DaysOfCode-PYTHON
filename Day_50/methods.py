# read(), readlines() and other methods | Python Tutorial - Day #50

# https://www.youtube.com/watch?v=l1FsnQxET9U&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=50

f = open('myfile.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in maths is: {m1}")
    print(f"Marks of student {i} in english is: {m2}")
    print(f"Marks of student {i} in hindi is: {m3}")
    
    print(line)