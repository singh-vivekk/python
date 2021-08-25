import pandas as pd
# import numpy as np
# printing the data frame
df = pd.read_csv('data.csv')
print("data is...")
print(df)
print()

# print the shape of data
print("Shape of data is: ", df.shape)
print()

# print first name and email
print("first_name and email is...")
print(df[['First_Name', 'Email']])
print()

# print the second and third row
print("second and third row is....")
print(df.iloc[[1, 2]])
print()

# print last_name, mobile number of 1 and 4 rows
print("last_name and mobile number of 1 and 4 rows is...")
print(df.iloc[[0, 3], [1, 3]])
print()

# to print all details of person based on first_name
print("details of Abhishek is...")
fil = (df['First_Name'] == 'Abhishek')
print(df.loc[fil])
print()

# to print specific details of person based on last_name
print("email and First_Name of people whose last name is Sharma...")
fil1 = (df['Last_Name'] == 'Sharma')
print(df.loc[fil1, ['Email', 'First_Name']])
print()
