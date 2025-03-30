def doubler(x):
	return x * 2

my_list = [1,1,23,4,5]
for item in map(doubler, my_list):
	print(item)


print(list(map(doubler,my_list)))


# using list comprehension
print([doubler(x) for x in my_list])


# use two lists
list_1=[1,2,3]
list_2=[4,5,6]

def add(x,y):
	return x + y

sum_lists = map(add, list_1, list_2)

print(list(sum_lists))