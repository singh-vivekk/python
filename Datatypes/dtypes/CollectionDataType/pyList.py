names = ["Aakash", "Vipul", "Amjad", "Amit", "Rahul", "Gaurav", "Kanchan", "Darshan"]

print(type(names))

# print(names)

# to add items to list:

names.append("Vikas")
newnames = ["Puneet","Suraj"]
# print(names)
# names.extend(newnames)
# print(names)

names.insert(5,"Kumar")   # costly operation - when we have a large list.
# print(names)

# List slicing:   name_of_list[start_position (inclusive) : end_position (exclude) : step=1]
# print(names[0])
# print(names[::])   # start : 0, end = last, step=1

myrng = [0,1,"Aakash",3,4,5,6,7,8,9,10]

# print(myrng[1::2])

# list comprehension
# myrng2=[x for x in range(10)]
# print(myrng2)

myrng3=[]     # empty list
print(myrng3)

for i in range(2,10,2):
    if i != 6:
        myrng3.append(str(i)+'-item')
    else:
        print("Value of i is 6 and not added to list")


print(myrng3)

myrng2=[str(x)+'-item' for x in range(0,10) if x !=6]
print(myrng2)


# [0-item, 2-item, 4-item, 6, 8]