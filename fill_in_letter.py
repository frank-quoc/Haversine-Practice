import pandas as pd

df = pd.read_csv('before_letters.csv')


dct = {
    'Atlanta Metropolitan Area, Georgia': (33.8498, -84.4383),
    'Greater Savannah Area, Georgia': (32.076176, -81.088371),
    'Greater Duluth Area, Georgia': (34.0029, -84.1446),
    ', Georgia 303010': (33.7600, -84.3900),
    'Greater Augusta Area, Georgia': (33.466667, -81.966667),
    'lpharetta, Georgia': (34.0754, -84.2941),
}

for i, row in df.iterrows():
    if row['Final City'] in dct.keys():
        df.at[i,'location_lat'] = dct[row['Final City']][0]
        df.at[i,'location_long'] = dct[row['Final City']][1]
        
nulls = df[df['location_lat'].isnull()]

df = df[df['location_lat'].notna()]
nulls.to_csv('./final/city_errors.csv', index=False)  
df.to_csv('atl_filled_.csv', index=False)  
