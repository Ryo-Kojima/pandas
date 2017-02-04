from pandas import Series,DataFrame

import pandas as pd

df = pd.read_csv("funish.csv")

df2 = df[(df.name == "禮田") | (df.name == "川路")]

print(df2)
