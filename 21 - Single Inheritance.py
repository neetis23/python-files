class Father:
    no_of_leaves = 30
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def print_details(self):
        print(f"The name is {self.name}, age is {self.age} and salary is {self.salary}")

class Child(Father):
    no_of_leaves = 20
     
fobj = Father("Ramesh", 45, 45000)
print(fobj.no_of_leaves)

cobj = Child("Kamlesh", 15, 30000)
print(cobj.no_of_leaves)
print(cobj.name)

fobj.print_details()
cobj.print_details()

