# Initializing

# class Employee:
# 	ID = 123
# 	department = "HR"
# 	salary = 4000

# John = Employee()

# print("ID: ", John.ID)
# print("department: ", John.department)
# print("salary: ", John.salary)


# Assigning
# class Employee:
#     # defining the properties and assigning them None
#     ID = None
#     salary = None
#     department = None


# # cerating an object of the Employee class
# Steve = Employee()

# # assigning values to properties of Steve - an object of the Employee class
# Steve.ID = 3789
# Steve.salary = 2500
# Steve.department = "Human Resources"

# # Printing properties of Steve
# print("ID =", Steve.ID)
# print("Salary", Steve.salary)
# print("Department:", Steve.department)



# Creating Properties outside Class

class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None


# cerating an object of the Employee class
Steve = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"
# creating a new attribute for Steve
Steve.title = "Manager"

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Title:", Steve.title)
