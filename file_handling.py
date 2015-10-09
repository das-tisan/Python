#!/usr/bin/env python

# File Open
file_object = open("file.txt","r+w")
#_________________________________________________

### File Manipulation  ###

#file_object.read()
#	read() reads the whole file
# 	if read() is used again then it will return empty string
#	hence it is better to read file line by line using readline()
print (file_object.readline())
# readline() reads single line 
# readlines() reads all lines

for x in file_object:
	print(x)
file_object.write("powerpork\n")
file_object.write("inddrag\n")
file_object.write("sanskran\n")


#_________________________________________________
#File close
file_object.close()