# Basic functions
import pandas as pd

pd.set_option('max_columns', None)

# create a dataframe
data = pd.read_csv("./data/nba.csv")
# print(data.dtypes)
#------------------------------------------------------------

# show a subset of dataframe
# print(data.head())


# df columns (df.columns)
# print(data.columns)


# drop columns
# df = data.drop(columns=['Number','Position','Height','College'])
# print(df.head())


# Length (len(df))
# print(len(data))


# Query (df.query())
# pd.set_option('max_columns', None)
# df = data.query("Number > Age")
# print(df.head())


'''
    iloc - to access records : slicing is possible
    This function takes as a parameter the rows and column indices and gives you the subset of the DataFrame accordingly
'''
row_start, row_end = 4, 8
column_start, column_end = 0, -1
# print(data.iloc[row_start:row_end, column_start:column_end])
# print(data.iloc[:, :])


'''
    loc - slicing is not possible
    This function does almost the similar operation as .iloc() function.
    But here we can specify exactly which row index we want and also the name of the columns we want in our subset
'''
# rows = [3, 10, 14, 23]
# columns = ['Name', 'Number', 'Age', 'Height']
# print(data.loc[rows, columns])
# print(data.loc[[3, 10, 14, 23], ['Name', 'Number', 'Age']])
# print(data[columns])


'''
    dtypes - to see the datatypes of each columns of dataframe,  a column or a list of columns 
'''
# print(data.dtypes)
# print(data.Name.dtypes)
# print(data[columns].dtypes)


'''
    df.select_dtypes()
'''
# You can select the variables or columns of a certain data type using this function
# print(data.select_dtypes(include='float64').head())


''' 
    df.insert - insert a new col at a specified position.
'''
import numpy as np
# random_col = np.random.randint(100, size=len(data))
# print(random_col)
random_col = range(len(data))
data.insert(2, 'random_col', random_col)   # no need for reassignment. it will modify the original dataframe
# print(data)


'''
    df[‘’].cumsum() : It provides you with the cumulative sum
'''
# print(data[['Number','Age']].head())
# print(data[['Number']].median())
# print(data[['Number','Age']].cumsum().head())


'''
    df.sample() - take a representative sample from it to perform the analysis and predictive modeling
'''
sample_data = data.sample(n=100)
# sample_data = data.sample(frac = 0.1)
# print(sample_data)
# print(len(sample_data))


'''
    df[‘’].where() - This function helps us to query a dataset based on a boolean condition 
'''
# print(sample_data['random_col'].where(sample_data['random_col'] > 300))
# print(sample_data['random_col'].where(sample_data['random_col'] > 300))
# print(sample_data['random_col'].where(sample_data['random_col'] > 300,0))


'''
    df[‘’].unique() - This is very useful where we have categorical variables. 
    It is used to find out the unique values of a categorical column
'''
# print(data.Team.unique())
# print(len(data.Team.unique()))

'''
    df[‘’].nunique() - This function lets us know how many unique values do we have in a column
    The great thing is, this function can be used on the total dataset as well to know the number of unique values in each column
'''
# print(data.Team.nunique())
# print(data.nunique())


'''
     df[‘’].rank() - This function provides you with the rank based on a certain column
'''
# print(data.nunique())
# data['rank_calc'] = data['Age'].rank()
# print(data.head())
# print(max(data.rank_calc))


'''
     isin() -  resulting dataset containing only those few records mentioned in the list above
     df[‘’].isin([list of values] or value)
'''
teams = ['Texas','Marquette', 'Georgia State']
df_filter = data['College'].isin(teams)
# print(df_filter)
# print(data[df_filter])


'''
     df.replace() -  It replaces the values of a column. 
     When we need to replace only one unique value of a column we simply need to pass the old value and the new value.
     Syntax: df.replace('existing_value', 'value to be replaced')
'''
# print(data[df_filter].replace('Texas', 'State-Texas').tail(20))
# print(data.replace('Texas', 'State-Texas').tail(20))


'''
    df.rename() - It is used to rename the column/s
    Syntax : df.rename(columns = {"Old_Col_1": "New_Col_1", "Old_Col_2": "New_Col_2", ...})
'''
# renamed_cols = {"College": "University", "Height": "Hgt"}
# print(data.rename(columns = renamed_cols))


'''
    .fillna() - This function .fillna() replaces the null values with some other value of your choice.
    Syntax: df['col'].fillna(0, inplace=True)
'''
# data['College'].fillna(data['random_col'].mean(), inplace=True)
# data['College'].fillna('-', inplace=True)
# print(data)


'''
    df.groupby() - This function .fillna() replaces the null values with some other value of your choice.
    Syntax: df.groupby("grouping_cols")['aggregate_cols'].aggregate_function()
'''
# df = data.groupby("College")['Salary'].max()
# print(df)

# print(data[data['College']=='Arizona']['Salary'].max())
print(data[data['College']=='Alabama'][['College','Salary']])
print(data[data['College']=='Alabama'][['Salary']].max())
# print(data[['Name', 'Number', 'Age']].head())

# columns = ['Name', 'Number', 'Age']
# print(data.loc[rows, columns])
# print(data[columns].head())

#Task: 
# create a dataframe.
# - apply pivot function
# - apply transpose function