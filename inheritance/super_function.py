# class Vehicle:  # defining the parent class
#     fuelCap = 90


# class Car(Vehicle):  # defining the child class
#     fuelCap = 50

#     def display(self):
#         # accessing fuelCap from the Vehicle class using super()
#         print("Fuel cap from the Vehicle Class:", super().fuelCap)

#         # accessing fuelCap from the Car class using self
#         print("Fuel cap from the Car Class:", Vehicle.fuelCap)


# obj1 = Car()  # creating a car object
# obj1.display()  # calling the Car class method display()

# Calling the parent class methods
class Vehicle:  # defining the parent class
    def display(self):  # defining display method in the parent class
        print("I am from the Vehicle Class")


class Car(Vehicle):  # defining the child class
    # defining display method in the child class
    def display(self):
        super().display()
        print("I am from the Car Class")


obj1 = Car()  # creating a car object
obj1.display()  # calling the Car class method display()
