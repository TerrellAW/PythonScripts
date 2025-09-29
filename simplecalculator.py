print("Simple Calculator")
num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))
# Listing valid operations ensures invalid ones are not typed
print("Choose an operation: ") 
print("add")
print("subtract")
print("multiply")
print("divide")

oper = str(input("> "))
match oper:
    case "add": # Adds numbers and stores "+" symbol in oper variable
        sol = num1 + num2
        oper = "+"
    case "subtract": # Subtracts numbers and stores "-" symbol in oper variable
        sol = num1 - num2
        oper = "-"
    case "multiply": # Multiplies numbers and stores "*" symbol in oper variable
        sol = num1 * num2
        oper = "*"
    case "divide": # Divides numbers and stores "/" symbol in oper variable
        sol = num1 / num2
        oper = "/"
    case _:
        print("Invalid Operation") # In case invalid operation is entered
print(f"{num1} {oper} {num2} = {sol}") # Prints the equation with mathematical symbols
print("Done")
input("> ")