# Function Arguments in Python | Python Tutorial - Day #21

# https://www.youtube.com/watch?v=0d6b6fFuCkE

# def average(a,b):
#     print("The average is ", (a+b) / 2)
# average(4,6)    


# DEFAULT ARGUMENTS

# def average(a = 1,b = 5):
#     print("The average is ",(a+b) / 2)
    
# average()    
# average(4,6)
# average(a = 10)


# REQUIRED ARGUMNETS

# def average(a, b = 5, c = 7):
#     print("The average is", (a+b+c) / 3)
    
# average(9)    


def average(*numbers):
    # print(type(numbers))
    
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)
    
c = average(4,5)     
print(c)


# def name (**name):
#     print(type(name))
    
#     print("Hello", name["fname"], name["mname"], name["lname"])

# name(fname = "Yash", mname = "Sanjeev", lname = "Halwai")