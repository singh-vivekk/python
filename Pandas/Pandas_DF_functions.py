'''
    Pandas DF - Basic Operations
'''

'''-- Create DF --'''
import pandas as pd
data=[['Tom', 10], ['Nick', 15], ['Juli', 14]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])

# print(df)

df1=df['Age'].apply(lambda x: str(x))
# print(df1)

'''-- Create List from DF --'''
df2=[str(i) for i in df['Age']]
# print(df2)

'''-- Create String from List --'''
df3=','.join(df2)
# print(df3)

df_row=df.iterrows()         # to create row object
df_records=df.to_records()
# print(type(df))
# print(type(df_row))
# print(type(df_records))

# print(df)
# print(df_row)
# print(df_records)

# df_row_list=[i for i in df.iterrows()]
# print(df_row_list)
print(df.iloc[2][1])
