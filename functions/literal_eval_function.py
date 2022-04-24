'''ast.literal_eval()
Python literal_eval is a function defined in “ast” class of built-in class library.
The “ast” expands to Abstract Syntax Tree.
The ast module helps Python applications to process trees of the Python abstract syntax grammar.

The literal_eval safely evaluate an expression node or a string containing a Python literal or container display.
The string or node (a file) provided may only consist of the following Python literal structures: strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None.

Limitation: literal_eval can recognize only one data type.
If the file contains elements having more than one data structure then it will throw an error.
Supported Python literal structures are strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None
'''
# Writing data to a file:
# dict1 = {'aipython': 2018, 'location': 'India', 'City':'Internet'}
# file_writer = open( r'C:\Users\Administrator\Desktop\myDictionary.txt', 'w+' )
# file_writer.write(str(dict1))
# file_writer.close()

# Reading data from a file:
# file_reader = open( r'C:\Users\Administrator\Desktop\myDictionary.txt', 'r' )
# print (file_reader.read())
# print (type(file_reader))

# # Reading data using literal_eval:
# import ast
# file_reader = open( r'C:\Users\Administrator\Desktop\myDictionary.txt', 'r' )
# temp_data   = ast.literal_eval( file_reader.read( ) )
# print (temp_data)
# print ("Data type of object is:  {}".format(type(temp_data)))
# print(temp_data['location'])

# # Reading data using eval:
# file_reader = open( r'C:\Users\Administrator\Desktop\myDictionary.txt', 'r' )
# temp_data_eval   = eval( file_reader.read( ) )
# print (temp_data_eval)
# print ("Data type of object using eval is:  {}".format(type(temp_data_eval)))


print("\n\n\n\n\n <><><><><><><><><><><><>")
# dict1 = {'aipython': 2018, 'location': 'India', 'City':'Internet'}
# print(type(dict1))
# str1 = str(dict1)

str1 ="'Chandra[', 'Sumit', 'Aakash]'"
print(type(str1))
print(str1)
print(str1[0:3])


new_str1 = eval(str1)
print(type(new_str1))


# print(list(dict.fromkeys(dict1)))