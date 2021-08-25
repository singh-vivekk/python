# The OS module in Python provides functions for interacting with the operating system.
# OS comes under Python’s standard utility modules.
# This module provides a portable way of using operating system-dependent functionality.
# The *os* and *os.path* modules include many functions to interact with the file system

# importing os module
import os

print("OS Name : "+os.name)

# Get the current working directory (CWD)
cwd = os.getcwd()

# Print the current working directory (CWD)
print("Current working directory:", cwd)

# -------------------- Changing the Current working directory: -----------------------------
def current_path():
    print("\nCurrent working directory : ")
    print(os.getcwd())
    print()

# Printing CWD before
current_path()

# Changing the CWD
os.chdir('../')

# Printing CWD after
current_path()

# ----------------------------  Creating a Directory  ---------------------------------------
# There are different methods available in the OS module for creating a directory
# os.mkdir()      - os.mkdir() method in Python is used to create a directory named path with the specified numeric mode.
#                 - This method raises FileExistsError if the directory to be created already exists.
# os.makedirs()   - os.makedirs() method in Python is used to create a directory recursively.
#                 - That means while making leaf directory if any intermediate-level directory is missing, os.makedirs() method will create them all.
# Python program to explain os.makedirs() method

# Leaf directory
directory = "Vivek"

# Parent Directories
# parent_dir = "D:/Pycharm projects/Base1/Authors"
parent_dir = os.getcwd()

# Path
path = os.path.join(parent_dir, directory)

os.makedirs(path)
print("Directory '% s' created" % directory)

# Directory 'Base1' and 'Authors' will be created too if it does not exists

# Leaf directory
directory = "c"

# Parent Directories
parent_dir = "D:/Pycharm projects/Base1/a/b"

# mode
mode = 0o666

path = os.path.join(parent_dir, directory)
# print(directory, " --- " , parent_dir, " --- ", path)
# Create the directory 'c'
os.makedirs(path, mode)
print("Directory '% s' created" % directory)

# 'GeeksForGeeks', 'a', and 'b' will also be created if it does not exists
# If any of the intermediate level directory is missing os.makedirs() method will create them
# os.makedirs() method can be used to create a directory tree


#########################################################
#### Listing out Files and Directories with Python  #####
#########################################################
# os.listdir() method in Python is used to get the list of all files and directories in the specified directory