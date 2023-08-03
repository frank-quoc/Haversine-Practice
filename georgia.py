import pandas as pd

personal_state = ['Georgia', 'GA']
state_region = [
    'GA', 
    'Ga', 
    'ga', 
    'GA - Georgia', 
    'GA Georgia', 
    'Atlanta GA',
    'Georgia', 
    'georgia',
    'Atlanta, Georgia',
    'Stone Mountain, Georgia',
    'GEORGIA',
    'GA Georgia',
]

state_us = 'Georgia'

LAT = 33.764048 
LONG = -84.393041
df = pd.read_csv('georgia.csv')

df = df.replace({
    'Personal State': {'GA': 'Georgia'},
    'State/Region': {
        'GA': 'Georgia',
        'Ga': 'Georgia',
        'ga': 'Georgia',
        'GA - Georgia': 'Georgia',
        'GA Georgia': 'Georgia',
        'Atlanta GA': 'Georgia',
        'georgia': 'Georgia',
        'Atlanta,Georgia': 'Georgia',
        'Stone Mountain,Georgia': 'Georgia',
        'GEORGIA': 'Georgia',
        'GA Georgia': 'Georgia',
    }
})
# Personal State. State/Region, State (U.S.)) 
df['Personal State'] = df['Personal State'].fillna(df.pop('State/Region'))
df['Personal State'] = df['Personal State'].fillna(df.pop('State (U.S.)'))
# rows_count = df.count()[0]
# print(f'NUM ROWS {rows_count}')

df = df.loc[df['Personal State'] == state_us]
# rows_count_2 = df.count()[0]
# print(f'Minus ROWS {rows_count_2}')

# print(df['Personal State'].unique())
# print(df.columns)

df['First Name'] = df['First Name'].fillna(df.pop('Form - First Name'))
df['Last Name'] = df['Last Name'].fillna(df.pop('Form - Last Name'))
df['Phone Number'] = df['Phone Number'].fillna(df.pop('Mobile Phone Number'))
df['Phone Number'] = df['Phone Number'].fillna(df.pop('Form - Phone Number'))
df['Job Title'] = df['Job Title'].fillna(df.pop('Form - Job Title'))
df['Company Name'] = df['Company Name'].fillna(df.pop('Form - Company Name'))
df['Personal City'] = df['Personal City'].fillna(df.pop('City'))
df['Personal City'] = df['Personal City'].fillna(df.pop('Form - City'))
df['Personal Zip Code'] = df['Personal Zip Code'].fillna(df.pop('Postal Code'))

# df.to_csv('georgia.csv', mode='w')
columns = ['Company Size (ZoomInfo)', 'Employee Range', 'Employee Size Zoom ', 'Number of Employees']

df_2 = df[columns]

print(df_2)