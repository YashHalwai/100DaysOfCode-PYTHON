# Exception Handling in Python | Python Tutorial - Day #36

# https://www.youtube.com/watch?v=4LKo6dlku7M&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=36

a  = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid input")