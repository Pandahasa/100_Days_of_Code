from turtle import clear


print("Welcome to the calculator")

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2
    
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
 }

calculating = True
while calculating:
    n1 = float(input("Enter your first number\n"))
    cont = True
    while cont:
        operator = input("What would you like to do, '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division\n")
        n2 = float(input("Enter your second number\n"))
        print("The result is" , operations[operator](n1,n2))
        if input("Do you want to continue with this number, 'y' for yes , or  'n' for no\n") == "y":
            n1 = operations[operator](n1,n2)
        else:
            cont = False
            clear()

       