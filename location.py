import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

from logger import get_logger

logger = get_logger('CurrUpdate')

geolocator = Nominatim(user_agent="myApp")

df = pd.read_csv('georgia.csv')
cols = ['Personal City', 'Personal State'] #'Personal Zip Code'
df['Combined City'] = df[cols].apply(lambda row: ', '.join(row.values.astype(str)), axis=1)
cols_2 = ['Combined City', 'Personal Zip Code']
df['Final City'] = df[cols_2].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
df['Final City'] = df['Final City'].map(lambda x: x.rstrip('nan,').lstrip(' nan').strip())
df = df.drop(['Combined City', 'Company Size (ZoomInfo)'], axis=1)
df['location_lat'] = np.nan
df['location_long'] = np.nan

df = df.drop(df.columns[[0, 1]],axis = 1)

# df[['location_lat', 'location_long']] = df['Personal Zip Code'].apply(
#     geolocator.geocode).apply(lambda x: pd.Series(
#         [x.latitude, x.longitude], index=['location_lat', 'location_long']))
df_2 = df.head()
for i, row in df.iterrows():
    try:
        location = geolocator.geocode(row['Final City'], country_codes="us")
        df.at[i,'location_lat'] = location.latitude
        df.at[i,'location_long'] = location.longitude
        df.to_csv('atl.csv')  
    except Exception as e:
        logger.error(row, exc_info=True)
        continue
    # row[['location_lat', 'location_long']] = row['Personal Zip Code'].apply(
    # geolocator.geocode).apply(lambda x: pd.Series(
    #     [x.latitude, x.longitude], index=['location_lat', 'location_long']))
# df.to_csv('atlanta.csv', mode='a')