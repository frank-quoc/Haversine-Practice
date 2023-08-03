import pandas as pd

df = pd.read_csv('null.csv')

df_2 = df[df['location_lat'].isna()]
rows_count = df_2.count()[0]
print(f'NUM ROWS 2 {rows_count}')
print(df_2['Final City'].unique())
print(df_2)
df_2.to_csv('./final/atl.csv')  