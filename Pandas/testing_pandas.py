# import pandas as pd
import pandas as pd

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is','portal', 'for', 'Geeks']

ser = pd.Series(lst)
# print(ser)
# Calling DataFrame constructor on list
# print("\n\n Dataframe: ")
df = pd.DataFrame(lst)
# print(df)

#------------------------------------------------------------
# intialize data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
# print(df)
#------------------------------------------------------------

# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# select two columns
# print(df)
# print(df[['Name', 'Qualification']])

#------------------------------------------------------------

# INDEX_COL: This is to allow you to set which columns to be used as the index of the dataframe.
# The default value is None, and pandas will add a new column start from 0 to specify the index column.
# It can be set as a column name or column index, which will be used as the index column.

# making data frame from csv file
# data1 = pd.read_csv("./data/nba.csv")
data = pd.read_csv("./data/nba.csv", index_col="Name")
# data = pd.read_csv("./data/nba.csv", index_col="Team")
# print(data1)
# print(data)
# print(data.dtypes)
# retrieving row by loc method
first = data.loc["Avery Bradley"]
# first = data.loc[0]
second = data.loc["R.J. Hunter"]
# second = data.loc[1]

# print(first, "\n\n\n", second)
#------------------------------------------------------------

# USECOLS: Specify which columns to import to the dataframe. It can a list of int values or column names.
# Reading Selected Columns from csv file
# data = pd.read_csv("./data/nba.csv", index_col=["Team","Number","Height"])
data = pd.read_csv("./data/nba.csv", usecols=["Team","Number","Height"])
# print(data)
#------------------------------------------------------------

# SEPARATOR: If you want to use another separator, simply add sep='\t' ;
# Default separator is ',' .
data = pd.read_csv('./data/pipedelimited.csv', sep='|')
# print(data)
#------------------------------------------------------------

# HEADER: this allows you to specify which row will be used as column names for your dataframe.
# Expected an int value or a list of int values.
# Default value is header=0, which means the first row of the CSV file will be treated as column names.
# If your file doesn’t have a header, simply set header=None
# df.read_csv('file_name.csv’, header=None) # no header
#------------------------------------------------------------

# NROWS: Only read the number of first rows from the file. Needs an int value.
data = pd.read_csv("./data/nba.csv", usecols=["Team","Number","Height"], nrows=10)
# data = pd.read_csv("./data/nba.csv", usecols=["Team","Number","Height"])
# print(data.dtypes)
# print(data)
# print(data.shape)

#------------------------------------------------------------

# CONVERTERS: Helps to convert values in the columns by defined functions.
f = lambda x: (x + '_converted_value')
df = pd.read_csv("./data/nba.csv", converters={'Position':f}, nrows=8)

# pd.set_option('display.max_columns', None)
# print(df)
# print(df.head())

# You can also use the string max_columns instead of display.max_columns(remember that it accepts a regex):
pd.set_option('max_columns', None)
# pd.set_option('max_columns', 2)
# print(df)

# To go back to the default value, you need to reset the option:
# pd.reset_option("max_columns")
print(df)

# max_colwidth :
print("*"*100)
# pd.set_option("max_colwidth", 15)
# print(df)


# ROWS : To change the number of rows you need to change the max_rows option.
pd.set_option("max_rows", 8)
print(df)