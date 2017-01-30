from pandas import Series,DataFrame

import pandas as pd

df = pd.read_csv("funish.csv",usecols=["sales"])

print(df.cumsum())