# from copy module
# Deepcopy stores copies of the object's value
# Shallow copy stores the reference of the objects to the original memory address

# Important Points:

import copy

##################### Deep Copy ###################################
#initializing the original list:
def deep_copy_method():
    Org_list = [1, 2, [7, 5], 4]

    #using deep copy to copy the values
    New_list=copy.deepcopy(Org_list)

    print("The original elements before deep copying :")
    for i in Org_list:
        print(i, end=" ")

    print("\r")
    # Adding an element to new list:
    New_list[2][1]='Updated value'

    print("Original List : ", Org_list)
    print("New list using deep copy : ", New_list)

# -- Deep Copy: Original List is unaffected by the changes in the new list
#######################################################

##################### Shallow Copy ###################################
#initializing the original list:
def shallow_copy_method():
    Org_list=[1,2,[7,5],4]

    #using copy to shallow copy
    sh_list=copy.copy(Org_list)

    print("The original elements before deep copying :")
    for i in Org_list:
        print(i, end=" ")

    print("\r")
    # Adding an element to new list:
    sh_list[2][1]='Updated value'

    print("Original List : ", Org_list)
    print("New list using shallow copy : ", sh_list)

# -- Shallow Copy: Original List is unaffected by the changes in the new list

#######################################################

print("\n\n******** Deep Copy ***********")
deep_copy_method()

print("\n\n******** Shallow Copy ***********")
shallow_copy_method()