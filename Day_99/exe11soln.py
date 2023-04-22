# Exercise 11: Solution + Shoutouts - Desktop Notification System | Python Tutorial - Day #99

# https://www.youtube.com/watch?v=18vZnLqXMoM&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=99


# import os

# import win10toast
from win10toast import ToastNotifier

# create an object to ToastNotifier class
n = ToastNotifier()

n.show_toast("GEEKSFORGEEKS", "You got notification", duration = 10)
