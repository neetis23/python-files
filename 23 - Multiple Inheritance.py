class Father:
    no_of_leaves = 30
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def print_details(self):
        print(f"The name is {self.name}, age is {self.age} and salary is {self.salary}")
        
class Mother:
    no_of_leaves = 20
    def __init__(self, name, age, sal):
        self.name = name
        self.age = age
        self.sal = sal
        
    def print_details(self):
        print(f"The name is {self.name}, age is {self.age}")
        
class Child(Mother, Father):
    pass


fobj = Father("Ramesh", 45, 45000)
print(fobj.name)

mobj = Mother("Sushma", 35, 34000)
print(mobj.name)

cobj = Child("Kamlesh", 15, 30000)
print(cobj.no_of_leaves)
print(cobj.name)

fobj.print_details()
mobj.print_details()
cobj.print_details()