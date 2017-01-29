import pandas as pd

df = pd.read_csv("funish.csv")

print(df.fillna({"sales":0}))