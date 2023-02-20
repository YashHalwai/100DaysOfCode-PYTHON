# seek(), tell() and other functions | Python Tutorial - Day #51

# https://www.youtube.com/watch?v=PByYX-2l5Us&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=51

# with open('file.txt', 'r') as f:
#     print(type(f))
    
#     # Move to the 10th byte in the file
    
#     f.seek(10)

#     # Read the next 5 bytes
    
#     data = f.read(5)
#     print(data)


# Truncate

with open('file.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(5)
    
with open('file.txt', 'r') as f:
    print(f.read())    