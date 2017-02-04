from pandas import Series,DataFrame

import pandas as pd

df = pd.read_csv("funish.csv")

df2 = df.groupby("team")

df3 = df2.sum()

print(df3)