################Set######################
# It can't have duplicates
# Unordered collection

my_set1 = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 5, 6}

# print(type(my_set1))
# print(dir(my_set1))

# print(dir(my_set1))   -- to see the applicable methods
#
print(my_set1.union(my_set2))
print(my_set1.intersection(my_set2))
# print(my_set2.issubset(my_set1))




my_list=[1,2,3,4,4,4,4,4,4,4,4,"aakash"]

uniq_num = set(my_list)
uniq_num_list = list(uniq_num)
print(uniq_num_list)
print(len(uniq_num_list))

# print(list(set(my_list)))
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