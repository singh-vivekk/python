import pandas as pd

index_df=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

# By using index in the pd.DataFrame, we can substitude the row index:
print(index_df)

# print(index_df.shape)
# We can use the shape attribute to check how large the resulting DataFrame is