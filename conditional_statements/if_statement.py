num = 5

if (num == 5): 
    print("The number is equal to 5") 

if num > 5:  
    print("The number is greater than 5")
    

# Compound conditional Statements

num = 12

if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
    # Only works when num is a multiple of 2, 3, and 4
    print("The number is a multiple of 2, 3, and 4")

if num % 5 == 0 or num % 6 == 0:
    # Only works when num is either a multiple of 5 or 6
    print("The number is a multiple of 5 or 6")
    

# Nested If Statements
num = 63

if num >= 0 and num <= 100:
    if num >= 50 and num <= 75:
        if num >= 60 and num <= 70:
            print("The number is in the 60-70 range")
            

# Creating and Editing Values:
num = 10
if num > 5:
    num = 20  # Assigning a new value to num
    new_num = num * 5  # Creating a new value called newNum

# The if condition ends; let’s check if the changes made inside it remain.
print(num)
print(new_num)



# Short Circuit Evaluation:
numerator = 10
denominator = 2
if denominator != 0:
    if numerator % denominator == 0:
        print("remainder is zero")
    print("denominator is zero")
    

if denominator != 0 and numerator % denominator == 0:
    print("remainder is zero")
    

numerator = 10
denominator = 0
if denominator == 0 or numerator % denominator == 0:
    print("Either the denominator is zero or remainder is zero.")