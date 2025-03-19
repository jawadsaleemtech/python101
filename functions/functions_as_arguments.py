def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function

# Using the calculator with the multiply function
print(calculataor(multiply, 10, 20)) 

# Using the calculator with the add function
result = calculator(add, 5, 3)
print(result)

# Assigning a function to a variable and passing it to the calculator
sub_var = subtract
print(calculator(sub_var, 10, 20)) 




# using lambdas
add = lambda a,b : a + b
subtract = lambda a,b : a - b
multiply = lambda a,b : a * b

def calculator(operation, n1, n2):
	return operation(n1,n2)


print(calculator(add,1,3))
print(calculator(subtract,1,3))
print(calculator(multiply,1,3))