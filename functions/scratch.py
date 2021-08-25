list1 = ['Hello', 'Hi', 'Hey']
print(list1)

listStr = "','".join(list1)
print(type(listStr))

print("'",listStr,"'")

# listStr2=str(list1)
# print(type(listStr2))
# print(listStr2)

# --------------------------------------

list2=['Hello','Hi','Hey']

print(list2)
list21='_'.join(list2)
print(list21)

print(list21.replace('_','|'))