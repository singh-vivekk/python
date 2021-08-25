# A Python program to demonstrate inheritance

# Different forms of Inheritance:
# 1. Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.
# 2. Multiple inheritance: When a child class inherits from multiple parent classes, it is called multiple inheritance.
# 3. Multilevel inheritance: When we have a child and grandchild relationship.

######################################################
#########      Example 1: Single Inheritance   #######
######################################################

print("""\n\n######################################################
#########      Example 1: Single Inheritance   #######
######################################################""")

# Base or Super class. Note object in bracket.(Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is equivalent to "class Person(object)"

class Person(object):
    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
    # Here we return true
    def isEmployee(self):
        return True


# Driver code
empP = Person("Geek1")  # An Object of Person
print(empP.getName(), empP.isEmployee())

empE = Employee("Geek2")  # An Object of Employee
print(empE.getName(), empE.isEmployee())




###############################################################
##########       Example 2: Inheritance  Example       ########
###############################################################

print("""\n\n###############################################################
##########        Example 2: Single Inheritance        ########
###############################################################""")
# Python code to demonstrate how parent constructors are called.

# parent class
class Person(object):
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
        print("from base class method")


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()

###############################################################
#########        Example 3: Multiple Inheritance        #######
###############################################################

print("""\n\n###############################################################
#########        Example 3: Multiple Inheritance        #######
###############################################################""")

# Python example to show the working of multiple
# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()


###############################################################
#########       Example 4: Multi-Level Inheritance      #######
###############################################################

print("""\n\n###############################################################
#########       Example 4: Multi-Level Inheritance      #######
###############################################################""")

class Base(object):
    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    # To get name
    def getAge(self):
        return self.age


# Inherited or Sub class (Note Person in bracket)
class GrandChild(Child):
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    # To get address
    def getAddress(self):
        return self.address


# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())


# 4. Hierarchical inheritance More than one derived classes are created from a single base.

# 5. Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.


###############################################################
#########   Example 4: Private members of parent class  #######
###############################################################

print("""\n\n###############################################################
#########   Example 4: Private members of parent class  #######
###############################################################""")

#
# We don’t always want the instance variables of the parent class to be inherited by the child class
# i.e. we can make some of the instance variables of the parent class private, which won’t be available to the child class.
# We can make an instance variable by adding double underscores before its name. For example,

# Python program to demonstrate private members
# of the parent class
class C(object):
	def __init__(self):
			self.c = 21

			# d is private instance variable
			self.__d = 42
class D(C):
	def __init__(self):
			self.e = 84
			C.__init__(self)
object1 = D()

# produces an error as d is private instance variable
# print(object1.d)
