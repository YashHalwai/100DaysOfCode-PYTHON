# Match Case Statements in Python | Python Tutorial - Day #16

# https://www.youtube.com/watch?v=bthQCK1QAmQ

x = int(input("Enter the Number:"))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x!=90:
        print(x, "is not 90")
    case _:
        print(x)    