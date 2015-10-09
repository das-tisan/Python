#!/usr/bin/env python3
import sys

if len(sys.argv) <3:
	print("Wrong parameter")
	print("./copy_file.py <source file> <dest file>")
	sys.exit(1)

file_object = open(sys.argv[1])
s=file_object.read()
file_object.close()

file_object=open(sys.argv[2],"w")
file_object.write(s)
file_object.close()


#	This way of reading file is not always a good idea, a file 
#	can be very large to read and fit in the memory. It is always 
#	better to read a known size of the file and write that to the 
#	new file.
