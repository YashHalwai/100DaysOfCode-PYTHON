# Regular Expressions in Python | Python Tutorial - Day #95

# youtube.com/watch?v=TCWOwavqFrw&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=95


import re

# pattern = r"[A-Z]+attern"

text = '''A regular expression is a pattern that the regular expression engine attempts to match in input text. A pattern consists of one or more character literals, operators, or constructs. For a brief introduction, see .NET Regular Expressions.

Each section in this quick reference lists a particular category of characters, operators, and constructs that you can use to define regular expressions.'''

# match = re.search(pattern,text)
# print(match)


# import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)