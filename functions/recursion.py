def factorial(num):
	if num == 0:
		return 1
	else: 
		return num * factorial(num-1)
	
result = factorial(4)
print(result)



def fibonacci(n):
    # Input validation
    if n < 1:
        return "Incorrect input, please enter a positive integer."
    
    # Base cases
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(fibonacci(6)) 