import pandas as pd

df = pd.read_csv("funish.csv")

df["gender_kana"] = df["gender"].map({1:"女性",2:"男性"})

print(df)