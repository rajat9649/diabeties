import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv('house price.csv')

profile=ProfileReport(df,title='pandas profiling report')
profile.to_file("house price.html")

