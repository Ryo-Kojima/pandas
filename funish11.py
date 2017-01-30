from pandas import Series,DataFrame

import pandas as pd

df = pd.read_csv("funish.csv")

df2 = pd.Series([17,"菅野",2,2,2,60000],index=["id","name","gender","grade","team","sales"])


print(df.append(df2,ignore_index=True))