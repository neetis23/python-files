# What is Method Overloading in Python?
# It is a form of Compile time polymorphism. In the case of method overloading, more than a single method belonging to a single class can share a similar method name while having different signatures. One can use method overloading for adding more to the behavior of concerned methods. A user won’t need more than one class for implementing it.

# Single Line Definition
# Method Overloading - A Function can be called with different number of arguments.

class VIP:
	def vsp(self, x=None, y=None):
		if x==None and y==None:
			print("Hello This is Python polymorphism")
		elif x!=None and y==None:
			f=1
			for i in range(1, x+1):
				f = f * i
			print(f)
		else:
			print("Addition is: ", x+y)

obj = VIP()
obj.vsp()
obj.vsp(5)
obj.vsp(6,7)