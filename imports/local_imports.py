import sys # global scope

def square_root(a):
	# local scope
	import math
	return math.sqrt(a)

def my_pow(base_num, power):
	return math.pow(base_num, power)

if __name__ == '__main__':
	print(square_root(49))
	# print(my_pow(2, 3))  # this will throw an error
else:
	print("Script called")