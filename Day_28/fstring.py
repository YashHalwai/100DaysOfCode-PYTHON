# f-strings in Python | Python Tutorial - Day #28

# https://www.youtube.com/watch?v=ixmxgUf8yIg&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=28


letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Harry"
# print(letter.format(name, country))


print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")


price = 49.09999
txt = "f For only {price: .2f} dollars!"
print(txt)


print(type(f"{2*30}"))