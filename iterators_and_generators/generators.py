def double_generator():
	number = 2

	while True:
		yield number
		number *= number

doubler = double_generator()

print(next(doubler))
print(next(doubler))
print(next(doubler))

print(type(doubler))