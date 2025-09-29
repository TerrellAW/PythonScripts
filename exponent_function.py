def power(base, exp): # Base and exponent parameters
    '''This function calculates base to the power of exp.'''
    print(f"{base:.2f}^{exp:.2f} = {base**exp:.2f}")
    result = base**exp
    return result

print("Example of program's function: ")
# Calls result variable from inside function outside of the function
result_outside = power(2,3) # 2 and 3 defined as arguments for base and exp parameters respectively

# Inputs with function
print("This program calculates the value of an exponential number.")
x = float(input("Enter a base number: "))
y = float(input("Enter an exponent number: "))

power(x,y)