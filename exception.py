try:
	fobj = open("hello.txt", "w")
	res = 12 / 0
except ZeroDivisionError:
	print("We have an error in division")
finally:
	fobj.close()
	print("Closing the file object.")