'''
    This code is to create a Pandas DF
    Sample code here to create a Pandas DF
'''
import pandas as pd

'''-- Create DF from List --'''

data=[['tom', 10], ['nick', 15], ['juli', 14]]
df_from_list = pd.DataFrame(data, columns = ['Name', 'Age'])

print(df_from_list)

'''-- Create DF from Dict 
        should have the same size of dict within --'''

d={'Ítems':['Pen','Pencil','Eraser','Sharpener'],'Cost':[15,10,5,4]}
df_from_dict=pd.DataFrame(d)

print(df_from_dict)

'''-- Create DF from File --'''
data=pd.read_csv("C:/Users/Administrator/PycharmProjects/data/python/sample.csv")
df_from_file=pd.DataFrame(data)

print(df_from_file)
print(df_from_file.shape)

# df_from_file.head()   #grabs the first five rows

# '''
#     The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify
#       example: index_col=0
# '''