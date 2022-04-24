import pandas as pd


pd_series=pd.Series([1, 2, 3, 4, 5])
print(pd_series)

pd_named_series=pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(pd_named_series)