def calculate(n, **kwargs):
	print(kwargs)

	for key,value in kwargs.items():
		print(f'key is {key} and value is {value}')

	n += kwargs["add"]
	n *= kwargs["multiply"]

	print(n)
calculate(5, add=3, multiply=5)



class Car:

	def __init__(self, **kw):
		self.make = kw.get("make")
		self.model = kw.get("model")
		self.year = kw.get("year")

my_car = Car(make="Nissan", model="GTR")
print(my_car.make)
print(my_car.model)
print(my_car.year)