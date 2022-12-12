# If Else Conditional Statements in Python | Python Tutorial - Day #14

# https://www.youtube.com/watch?v=ceiuLR2ysas

# conditional operators
# > < >= <= == !=

# applePrice = 190
# budget = 200

# if(budget - applePrice > 50):
#     print("Alexa, add 1 kg apples to the cart")
# elif(budget - applePrice > 70):
#     print("Its okay you can buy")    
# else:
#     print("Alexa, do not add apples to the cart")    



num = int(input("Enter the value of num: "))
if(num < 0):
    print("Number is negative.")
elif(num == 0):
    print("Number is zero.")    
elif(num == 999):
    print("Number is special.")    
else:
    print("Number is positive.")    