import pandas as pd

df = pd.read_csv("funish.csv",usecols=["name"])

print(df.drop(13))