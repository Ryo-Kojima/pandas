from pandas import Series,DataFrame

import pandas as pd

df = pd.read_csv("funish.csv")

df2 = df[(df.id == 2) | (df.id == 3)]

print(df2)
