def add(n1,n2):
	try:
		result = n1+n2
	except:
		print("exception: wrong number added")
	finally:
		print("all went well")
		print(result)
	
add(10,20)


number1=10
number2 = input("please enter a number: ")

add(number1,number2)