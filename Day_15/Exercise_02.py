# Exercise 2: Good Morning Sir | Python Tutorial - Day #15

# https://www.youtube.com/watch?v=d7ng_aV4qdI

'''
Q. Create a python program capable of greeting you with Good Morning,
   Good Afternoon, Good Evening, and Good Night. 
   Your program should use time module to get the current hour.
==>
'''

import datetime
now = datetime.datetime.now()
hour = now.hour

if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good night"

# print(now)
print("{}!".format(greeting))