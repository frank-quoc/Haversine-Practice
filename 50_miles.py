import pandas as pd

#Initialize DataFrame
df = pd.read_csv('atl_filled_.csv')

#Atlanta center point
newlat=33.764048 
newlon=-84.393041

#Import trig stuff from math
from math import sin, cos, sqrt, atan2,radians

#Distance function between two lat/lon
# Haversine formula
def getDist(lat1,lon1,lat2,lon2):
  R = 6373.0

  lat1 = radians(lat1)
  lon1 = radians(lon1)
  lat2 = radians(lat2)
  lon2 = radians(lon2)

  dlon = lon2 - lon1
  dlat = lat2 - lat1

  a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
  c = 2 * atan2(sqrt(a), sqrt(1 - a))

  return R * c

#Apply distance function to dataframe
df['dist']=list(map(lambda k: getDist(df.loc[k]['location_lat'],df.loc[k]['location_long'],newlat,newlon), df.index))
#This will give all locations within radius of 50 MILES
df = df[df['dist']<80.4672]

df.to_csv('under_50_miles.csv', index=False)