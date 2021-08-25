#Hello world module:
print("Hello World")

#Defining a variable in python:
fname="vivek"
# new_items= no_of_items*5
# print(fname[::2])
# print(new_items)

# List/Set/Tuple
# []
# no_list=[1,2,3,4,5,6,7,8,9,10,"Hello"]
#length
# print(len(no_list))

#Append / Extend
new_val=[1,2,3,4]
print(dir(new_val))
# no_list.append(new_val)

# no_list.extend(new_val)

# print(no_list)

# for x in no_list:
#     if x%2==0:
#         print(x)


############TUPLE#####################
my_tuple=(1,2,3,new_val, (43,76),3,3,3,3)

# del my_tuple

# print(dir(my_tuple))

# print(my_tuple.count(3))
# print(my_tuple.index(3))

# print(1 not in my_tuple)

################Set######################
#it can't have duplicates

my_set={1,2,3,4,4,4,4,4,4,4,4}
# print(type(my_set))
# print(dir(my_set))
# print(my_set)
#
# city_names=["Pune", "Mumbai", "Nagpur", "Nashik", "Nashik"]
# print(city_names)
#
# print("\n\n")
# distinct_city_names=list(set(city_names))
#
# print(type(distinct_city_names))
# print(distinct_city_names)
#Type casting
# no_of_items="5"
# print(type(no_of_items))
# print(int(no_of_items)*5)

#Dict
#
# my_dict={1:"first", 2:"Second", 3:"Third", 1:"last" }
# print(type(my_dict))
# print(my_dict[1])



if __name__=='__main__':
    print("executing from helloworld.py")

