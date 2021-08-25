# Python Class:
# A class is a user-defined blueprint or prototype from which objects are created.
# Classes provide a means of bundling data and functionality together

print("""\n\n###################################
#####  Example : Python Class #####
###################################""")

# Example:
class Test:
    pass

#Class Body:
class Car():

    # A simple class attribute
    attr1 = "Attribute_1"
    attr2= "Attribute_2"

    def printCarName(self, brand):
        print("Car Brand is : {0}".format(brand))

    def printCarColor(self, color):
        print("Car color is : {0}".format(color))



# Object instantiation
# An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values

CarObj=Car()

print(CarObj.attr1)
CarObj.printCarName('Volkswagon')
CarObj.printCarColor('Blue')


# ----------------------------------------------------------------------
# __init__ method example:

print("""\n\n###################################
#### Example __init__ method:  ####
###################################""")

# A Sample class with init method
class Company:
    # init method or constructor
    def __init__(self, name='noname'):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my organisation name is', self.name)


p = Company()
p.say_hi()

print("""\n\n###################################
#### Example :Variable no. of arguments  ####
###################################""")

#args
#kwargs

def myMethod(arg1, *argv):
    for agr in argv:
        print(agr)

# myMethod('Vivek','hello')

def myKwarg(name, **kwargs):
    for key, value in kwargs.items():
        print(" %s == %s" % (key, value))


myKwarg("LTI", first='Reetank', second='SaiSushma', third='Swetha')
