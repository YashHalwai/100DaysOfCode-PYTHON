# Snake Water Gun Game in Python - Exercise 5 - Solution | Python Tutorial - Day #63

# https://www.youtube.com/watch?v=GkfBpm6MN9A&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=63

import random

def check(comp, user):
    
    if comp == user:
        return 0
    
    if(comp == 0 and user == 1):
       return -1
    
    if(comp == 1 and user == 2):
        return -1
    
    if(comp == 2 and user == 0):
        return -1
    
    return 1
   
comp = random.randint(0,2)
user = int(input("0 for Snake, 1 for Water, and 2 for Gun: \n"))    


score = check(comp, user)

print("You: ", user)
print("computer: ", comp)

if(score == 0):
    print("Its a draw")
elif(score == -1):
    print("You Lose")
else:
    print("You Won")        