import pandas as pd
from geopy.geocoders import Nominatim

from logger import get_logger

logger = get_logger('CurrUpdate')

geolocator = Nominatim(user_agent="myApp2")

df = pd.read_csv('atl.csv')
rows_count = df.count()[0]
# print(f'NUM ROWS {rows_count}')
# df_2 = df[df['location_lat'].isnull()]
# # rows_count = df_2.count()[0]
# # print(f'NUM ROWS 2 {rows_count}')

# # df_3 = df[df['location_lat'].isna()]
# # rows_count = df_3.count()[0]
# # print(f'NUM ROWS 2 {rows_count}')
# print(df_2['Final City'].unique())


# rows_count = df.count()[0]
# print(f'NUM ROWS {rows_count}')



nulls = df[(df['location_lat'].isnull()) & (df["Personal Zip Code"].notnull())]
for i, row in nulls.iterrows():
    try:
        location = geolocator.geocode(row['Personal Zip Code'], country_codes="us")
        nulls.at[i,'location_lat'] = location.latitude
        nulls.at[i,'location_long'] = location.longitude
        nulls.to_csv('null.csv', index=False)  
    except Exception as e:
        logger.error(row, exc_info=True)
        continue

    # location = geolocator.geocode(row['Personal Zip Code'])
    # df.at[i,'location_lat'] = location.latitude
    # df.at[i,'location_long'] = location.longitude

# rows_count = df_2.count()[0]
# print(f'NUM ROWS 2 {rows_count}')
# df_2 = df[df['location_lat'].isnull()]

# def new_column(df1):
#     if (df['location_lat'].empty and df['Final City'] == 'Atlanta Metropolitan Area, Georgia'):
#         df['location_lat'] = 33.8498
#         df['location_long'] = -84.4383

# df = df.apply(new_column)

# print(df)
# df_2 = df[df['location_lat'].isna()]
# # df['Normalized'] = df.apply(lambda row : normalise_row(row), axis=1) 

# print(df_2['Final City'].unique())