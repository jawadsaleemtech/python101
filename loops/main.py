def multiplication_table(n):
  # Write you code here
	for i in range(1,11):
		for j in range(1,11):
			multiply = i*j
			print (f"{i} * {j} is {multiply}")
			

multiplication_table(5)