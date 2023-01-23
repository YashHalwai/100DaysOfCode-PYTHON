# Set Methods in Python | Python Tutorial - Day #32

# https://www.youtube.com/watch?v=HOrutCnp2zo&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=32

# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.union(s2)) # UNION METHODS 
# s1.update(s2)
# print(s1, s2)


# cities = {"T", "M", "B", "D"}
# cities2 = {"T", "S", "K", "M"}
# cities.intersection_update(cities2)
# print(cities)


# cities = {"T", "M", "B", "D"}
# cities2 = {"T", "S", "K", "M"}
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)


# cities = {"T1", "M", "B", "D"}
# cities2 = {"T", "S", "K", "M1"}
# cities3 = cities.isdisjoint(cities2)
# print(cities3)


# cities = {"T", "M", "B", "D"}
# cities2 = {"T", "S", "K", "M"}
# cities3 = cities.issuperset(cities2)
# print(cities3)


# cities = {"T", "M", "B", "D"}
# cities2 = {"T", "M"}
# cities3 = cities.issuperset(cities2)
# cities4 = {"A", "B"}
# cities5 = cities4.issuperset(cities)
# print(cities3)
# print(cities5)


# cities = {"A", "B"}
# cities.add("C")
# print(cities)