# # private properties
# class Employee:
#     def __init__(self, ID, salary):
#         self.ID = ID
#         self.__salary = salary  # salary is a private property


# Steve = Employee(3789, 2500)
# print("ID:", Steve.ID)
# print("Salary:", Steve.__salary)  # this will cause an error


class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displaySalary()
# Steve.__displayID()  # this will generate an error
Steve._Employee__displayID()  # this will generate an error
