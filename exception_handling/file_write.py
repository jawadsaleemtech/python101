try:
	f = open("testfile.txt", 'w') # if 'r' it will raise OS error
	f.write("write a test line")
except TypeError:
	print("there was an err writing file")
except OSError:
	print("Hey you have OS error")
except:
	print("All other exceptions!")
finally:
	print("I always run")