import pandas as pd


df = pd.read_csv('georgia.csv')

columns = ['Company Size (ZoomInfo)', 'Employee Range', 'Employee Size Zoom ', 'Number of Employees']

df_2 = df[columns]


test = df_2[~df_2['Employee Range'].isna()]

print(test)


