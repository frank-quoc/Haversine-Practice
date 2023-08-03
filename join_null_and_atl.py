import pandas as pd

df_main = pd.read_csv('atl.csv')
# df_main = df_main.drop(df_main.columns[[0]],axis = 1)
# print(df_main)
# print(list(df_main.columns))

df_nulls = pd.read_csv('null.csv')
# df_nulls= df_nulls.drop(df_nulls.columns[[0]],axis = 1)
# print(df_nulls)
# print(list(df_nulls.columns))
# df = pd.merge(df_main, df_nulls, how='left', on = 'Unnamed: 0')
# print(df)

# df = pd.concat([df_main, df_nulls], axis = 1)
# print(df)
# df_main['location_lat'] = df_main['location_lat'].fillna(df_nulls.pop('location_lat'))
# df_main['location_long'] = df_main['location_long'].fillna(df_nulls.pop('location_long'))
df_main = df_main.set_index('Unnamed: 0').fillna(df_nulls.set_index('Unnamed: 0')).reset_index()

df_main.to_csv('before_letters.csv', index=False)
