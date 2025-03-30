def greater_than_5(x):
	return x > 5

my_list = [1,2,3,4,5,10,20,40]

for item in filter(greater_than_5, my_list):
	print(item)
