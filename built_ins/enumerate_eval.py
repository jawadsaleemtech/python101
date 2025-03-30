my_str = 'HelloWorld'
for pos, letter in enumerate(my_str):
	print(pos, letter)


list1 = ['enumerate', 'method', 'being', 'used', 'with', 'a', 'list']
print(list(enumerate(list1)))


# setting custom index
my_string = 'abcdefg'
print (list(enumerate(my_string, -2)))


# EVAL
var = 10
source = 'var * 2'
print (eval(source))