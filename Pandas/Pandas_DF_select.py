# https://www.geeksforgeeks.org/how-to-randomly-select-rows-from-pandas-dataframe/
# Selects one row randomly using sample() without give any parameters.

# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku'],
		'Age':[27, 24, 22, 32, 15],
		'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
		'Qualification':['Msc', 'MA', 'MCA', 'Phd', '10th']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

print(df.shape)

# Select one row randomly using sample() without give any parameters
print(df.sample())

# To get 3 random rows each time it gives 3 different rows
# df.sample(3) or
print(df.sample(n = 3))


# Using Frac parameter:
# here you get .50 % of the rows
df.sample(frac = 0.5)


# Select more than rows with using replace
# default it is False
print(df.sample(n = 6, replace = True))
print(df.sample(n = 6, replace = False))