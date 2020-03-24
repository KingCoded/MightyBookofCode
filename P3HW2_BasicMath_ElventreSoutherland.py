#This program will create a calculator that can add,
    #multiply and divide
# CTI-110
# P3HW2 - BasicMath
# Elventre' Southerland
# 3/19/20
#

#Define a function that adds two numbers
def add(x, y):
            return x + y

#Define a function that subtracts two numbers
def subtract(x, y):
            return x - y

#Define a function that mutliply two numbers
def multiply(x, y):
            return x * y

#Define a function that divides two numbers
def divide(x, y):
            return x / y
#Display mathematic operations for users to choose from
print("This is a basic Calculator! Please Select an Operation.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#Variables: num1, num2, choice
#Get input from user
choice = input("Enter choice {1_2_3_4}: ")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))

if choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == "3":
        print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == "4":
        print(num1, "/", num2, "=", divide(num1, num2))

else:
        print("Invalid Input")

    
















