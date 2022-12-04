# Exercise 1: Calculator using Python | Python Tutorial - Day #7

# https://www.youtube.com/watch?v=FLVqcxnJP_E&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=7

# Create a calculator capable of performing addition, subtraction, multiplication, and division operations
# on two numbers.
# Your program should format the output in a readable manner!

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

choice = input("Choose an operator:\n 1) + \n 2) - \n 3) * \n 4) / \n: ")

if choice == '+':
    print("Addition: ", (num1 + num2))
    
elif choice == '-':
    print("Subtraction: ", (num1 - num2))    
    
elif choice == '*':
    print("Multiplication: ", (num1 * num2))    
    
elif choice == '/':
    print("Division ", (num1 / num2)) 

else:
    print("Please enter valid operator")       
    
    