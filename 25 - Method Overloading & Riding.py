# Method Overloading Vs. Method Overriding: 
# What is the Difference Between Method Overloading and Method Overriding in Python?

# What is Method Overloading in Python?
# It is a form of Compile time polymorphism. In the case of method overloading, more than a single method belonging to a single class can share a similar method name while having different signatures. One can use method overloading for adding more to the behavior of concerned methods. A user won’t need more than one class for implementing it.

# Note – Python does not provide any support for method overloading. A user may overload all the methods, but they will be capable of using only the latest defined method.

# What is Method Overriding in Python?
# It is a type of run-time polymorphism. In the case of method overriding, the child class provides a specific implementation of any method (that the parent class already provides). Method overriding assists a user in changing the behavior of already existing methods. One needs at least two classes to implement it. Inheritance is also a prerequisite in method overriding. It is because it occurs between both the methods- superclass (parent class) and child class.

# Difference Between Method Overloading and Method Overriding in Python
# ---------------------------------------------------------------------------
# Definition
# ----- In the process of method overloading, all the functions or methods must contain the same name with varied signatures.
# ----- In the process of method overriding, all the functions or methods must possess the very same name along with similar signatures.

# Type of Polymorphism
# ----- It comes under compile-time polymorphism.
# ----- It comes under run-time polymorphism.

# Inheritance
# ----- One may or may not require inheritance in the case of method overloading.
# ----- Inheritance is a prerequisite in the case of method overriding.

# Number of Classes
# ----- A user won’t need more than one class for implementing method overloading.
# ----- A user would always require at least two classes for implementing method overriding. It always works with more than one class.