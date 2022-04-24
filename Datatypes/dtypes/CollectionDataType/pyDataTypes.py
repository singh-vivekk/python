'''
    Basic of Python
    Print statement
    Python version
    Data Types
'''
print("***************  Python Data Types *******************")


#List
pyList=['first','second','third','second']
print(type(pyList))
print(pyList)

# in memory - memory consumption.
# Generators
# List comprehension =

#To convert a list into a string
allValues="-".join(pyList)
print(type(allValues))
print(allValues)

#DataTypes: List/Set/Tuple/Dict

# list is a ordered collection, it can have duplicates
print(pyList)

# set - as list but it doesn't contains duplicates
list123=list(set(pyList))
print(list123)
print(type(list123))

# set1={'first', 'second','third','second'}
# print(type(set1))
# print(set1)

# tuple is immutable collection:
tp1=('a','b')
print(type(tp1))
