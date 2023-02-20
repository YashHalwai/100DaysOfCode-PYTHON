# Map, Filter and Reduce in Python | Python Tutorial - Day #53

# https://www.youtube.com/watch?v=OErhjT4f5Cs&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=53


def cube(x):
    
    return x * x * x 

print(cube(2))


l = [1,2,4,5,6,7,6,5]


# newl = []
# for item in l:
#     newl.append(cube(item))

# # MAP

# newl = list(map(cube, l))
# print(newl)


# # FILTER


# def filter_function(a):
#     return a > 2

# newnewl = list(filter(filter_function,l))
# print(newnewl)


# # REDUCE

from functools import reduce

# List of numbers
numbers = [1,2,3,4,5]

# Calculate the sum of the numbers using reduce function
sum = reduce(lambda x,y : x + y, numbers)

# Print the sum
print(sum)