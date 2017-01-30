from pandas import Series,DataFrame

import pandas as pd

df = pd.read_csv("funish.csv")

df["sales_1000"] = df["sales"] / 1000

print(df)