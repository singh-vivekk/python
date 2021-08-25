

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


# Close opend file
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
