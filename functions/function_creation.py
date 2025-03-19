def my_print_function():  # No parameters
    print("This")
    print("is")
    print("A")
    print("function")
# Function ended


# Calling the function in the program multiple times
my_print_function()
my_print_function()


# Parameters

def minimun(first, second):
    if (first < second):
        print(first)
    else:
        print(second)
        

num1 = 10
num2 = 20

minimun(10,20)


# Return Statement
def minimum(first, second):
    if (first < second):
        return first
    return second


num1 = 10
num2 = 20

result = minimum(num1,num2)  # Storing the value returned by the function
print(result)