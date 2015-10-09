#!/usr/bin/env python3

class Person(object):
	def __init__(self,name):
		self.name = name

	def get_details(self):
		return self.name

class Student(Person):
	def __init__(self,name,branch,year):
		Person.__init__(self,name)
		self.branch = branch
		self.year = year

	def get_details(self):
		return "%s studies %s and is in %s year." %(self.name,self.branch,self.year)

class Teacher(Person):
	def __init__(self,name,papers):
		Person.__init__(self,name)
		self.papers = papers

	def get_details(self):
		return "%s teaches %s" %(self.name,'.'.join(self.papers))

person1 = Person("Sachin")
student1 = Student("Tisan","CSE",2011)
teacher1 = Teacher("Avijit",["DS","TOC"])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())	

del person1
del student1
del teacher1
"""
del actually decreases reference count by one. When the reference 
ount of an object becomes zero the garbage collector will delete 
that object
"""
