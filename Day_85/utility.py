# Creating command line utility in python | Python Tutorial - Day #85

# https://www.youtube.com/watch?v=3IAu6-pgw7I&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=85

# Tutorial => https://replit.com/@codewithharry/85-Day-85-Command-Line-Utility#.tutorial/Tutorial.md


"""
Command line utilities are programs that can be run from the terminal or command line interface, and they are an essential part of many development workflows. In Python, you can create your own command line utilities using the built-in argparse module.
"""


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--optional", help="description of optional argument", default="default_value")
args = parser.parse_args()
print(args.optional)

"""
Creating command line utilities in Python is a straightforward and flexible process thanks to the argparse module. With a few lines of code, you can create powerful and customizable command line tools that can make your development workflow easier and more efficient. Whether you're working on small scripts or large applications, the argparse module is a must-have tool for any Python developer.
"""