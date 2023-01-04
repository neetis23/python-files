# What is Method Overriding in Python?
# It is a type of run-time polymorphism. In the case of method overriding, the child class provides a specific implementation of any method (that the parent class already provides). Method overriding assists a user in changing the behavior of already existing methods. One needs at least two classes to implement it. Inheritance is also a prerequisite in method overriding. It is because it occurs between both the methods- superclass (parent class) and child class.

# Single Line Definition
# Multiple function with same name and same number of parameters

class A:
	def vsp(self):
		print("hi")

class B:
	def vsp(self):
		print("hello")
	def xyz(self):
		print("Good Morning")

ob = B()
ob.vsp()