# String Methods in Python | Python Tutorial - Day #13

# youtube.com/watch?v=0INvoK_T0cE


#  STRINGS are immutable

# a = "!!! Harry !!!!!"

# print(len(a))

# print(a.upper())

# print(a.lower())


# not affect the exist string but makes new string.

# print(a.rstrip("!")) # end part removes 

# print(a.replace("Harry", "John")) # all occurrence are replace

# print(a.split()) # convert into list


# intro = "introductiOn to Js"

# print(intro.capitalize()) # only first character to uppercase of sentence (Blogs)


# str1 = "Welcome to Course"
# print(str1.center(50))
# print(len(str1))
# print(len(str1.center(50)))


# name = "Yash Yash !!!!! 100 Days of Code"
# print(name.count("Yash"))


# str2 = "Welcome !!!"
# print(str2.endswith("!!!"))


# str2 = "Welcome to Challenge !!!"
# print(str2.endswith("to", 4, 10))


# str3 = "He is a good boy"
# print(str3.find("is")) # if not find -1
# print(str3.index("isa"))


# name = "WelcomeToTheCourse"
# print(name.isalnum()) # A-Z a-z 0-9


# name = "WelcomeToTheCourse5"
# print(name.isalpha()) # A-Z a-z  (0-9 is present then it returns FALSE)


# str1 = "hello world"
# print(str1.islower())


# str1 = "Wish you a Merry Christmas\n"
# print(str1.isprintable())
# print(str1)
# str1 = "Wish you a Merry Christmas"
# print(str1.isprintable())


# str1 = "    " # using spacebar
# print(str1.isspace())

# str1 = "        " # using tab
# print(str1.isspace())


# title1 = "Yash Sanjeev Halwai"
# print(title1.istitle())


# s = "Python is a Interpreted Language"
# print(s.startswith("Python"))


# s = "Python is a Interpreted Language"
# print(s.swapcase()) # upper to lower || vice-versa


# s = "Python is a Interpreted Language"
# print(s.title())