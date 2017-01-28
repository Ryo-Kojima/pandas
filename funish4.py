import pandas as pd

df = pd.read_csv("funish.csv",usecols=["gender","grade"])

print(df)