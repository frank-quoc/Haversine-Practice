import pandas as pd


df = pd.read_csv('under_50_miles.csv')

columns = ['Company size', 'Employee Range', 'Employee Size Zoom ', 'Number of Employees']

df_2 = df[columns]

for col in df_2:
  print(df_2[col].unique())