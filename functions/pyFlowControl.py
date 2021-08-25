mode=str(input("Enter mode: "))

# Case comparision and conversion:
print(mode)
print(mode.upper())
print(mode.lower())
print(mode.isupper())
print(mode.islower())

mode=mode.upper()

####################
### If statement ###
####################
if mode=='STR':
    print("Strategic mode")
elif(mode=='STD'):
    print("Standard mode")
else:
    raise Exception("Please enter thes valid mode - STR or STD")