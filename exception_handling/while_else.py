while True:
	try:
		number = int(input("please enter a number: "))
	except:
		print("This is not a number")
		continue
	else:
		print("in else block")
		break
	finally:
		print("in finally")