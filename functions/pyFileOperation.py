# different modes:
# With file access mode 'a'

# Open a file with append as access mode 'a' and write data to it
with open("sample.txt", "a") as file_object:
    # Append 'hello' at the end of file
    file_object.write("hello")


# Open the file in append & read mode ('a+')
with open("sample2.txt", "a+") as file_object:
    # Move read cursor to the start of file.
    file_object.seek(0)
    # If file is not empty then append '\n'
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    # Append text at the end of file
    file_object.write("hello hi")


# Open a file
fo = open("Definition_Python_concepts", "r+")
position = fo.tell()
print ("Current file position : ", position)
str = fo.read(50);
print("Read String is : ", str)

# Check current position
position = fo.tell()
print ("Current file position : ", position)

# Read next 50 lines of the file
str = fo.read(50);
print("Read String is : ", str)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(30)
print ("Again read String is : ", str)

# Reposition pointer to an arbitarary place
position = fo.seek(1, 0);
position = fo.tell()
print ("offset file position : ", position)
str = fo.read(30)
print ("Pointer positioned at : ", str)


# Close opened file
fo.close()


# Open a file
# wb : Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# fo = open("foo.txt", "wb")
# fo.write( "Python is a great language.\nYeah its great!!\n")
# print("Name of the file: ", fo.name)
# print("Closed or not : ", fo.closed)
# print("Opening mode : ", fo.mode)
# print("Softspace flag : ", fo.softspace)
fo.close()

import os
# Rename a file from test1.txt to test2.txt
os.rename(  "bar.txt", "foo.txt" )
os.rename( "foo.txt", "bar.txt" )

# Delete file bar.txt
os.remove("bar.txt")

# Create a directory "test"
os.mkdir("test")

# Changing a directory to "/home/newdir"
os.chdir("/home/newdir")

# This would give location of the current directory
os.getcwd()

# This would  remove "/tmp/test"  directory.
os.rmdir( "/tmp/test"  )
