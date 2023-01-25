# Exercise 4: Secret Code Language | Python Tutorial - Day #40

# https://www.youtube.com/watch?v=pOWJ6WgVRIU&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=40

# Write a python program to translate a message into secret code language.
# Use the rules below tp translate normal English into secret code language.

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:
#     simply reverse the string

# Decoding
# if the word contains less than 3 characters, reverse it
# else:
#     remove 3 random characters from start and end. Now remove the last letter and append it to the beginning.

# Your program should ask whether you want to code or decode

a = input ("Enter the message : ")
import random
H = random.choice(["dhj" , "jkh" ,"rty"])
B = random.choice(["abc","tyu","iop"])
print(B+a[1:len(a)]+a[0:1]+H)

print("for decode add two No:")
import random
C = random.choice([3,5,7,9])
D = random.choice([1,2,4,5])
print(C)
print(D)
F = int(input ("enter the no :"))
if  ( F==C+D) :
    print(a)
else :
   print("you are wrong")