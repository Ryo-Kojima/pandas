from pandas import Series,DataFrame

import pandas as pd

df = pd.read_csv("funish.csv")
df2 = pd.read_csv("funish_team.csv")
print(df2)
df3 = pd.merge(df,df2,left_on="team",right_on="team_no",how="inner",suffixes=("_x","_y"))
print(df3)