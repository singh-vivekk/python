import pandas as p
d={'Ítems':['Pen','Pencil','Eraser','Sharpener'],'Cost':[15,10,5,4]}
print('Creating Data Frame for a Dictionary')
df=p.DataFrame(d)
print('The Data Frame for Dictionary is \n')
print(df)
print('Creating Data Frame for csv file')
data=p.read_csv("C:/Users/hp/PycharmProjects/pythonProject1/sample.csv")
df1=p.DataFrame(data)
print('The Data Frame for csv file is \n')
print(df1)
