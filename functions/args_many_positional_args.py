def add(n1,n2):
	return n1+n2


# print(add(1,2))


def add(*args):
	sum = 0
	for n in args:
		sum +=n
	return sum

print(add(1,2,3,4,5))
	