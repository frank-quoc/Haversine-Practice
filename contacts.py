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
df = pd.read_csv('all-contacts.csv')

col = [
    "First Name",
    "Last Name",
    "City",
    "Company Name",
    "Company size",
    "Company Size (ZoomInfo)",
    "Email",
    "Employee Range",
    "Employee Size Zoom ",
    "Form - City",
    "Form - Company Name",
    "Form - First Name",
    "Form - Job Title",
    "Form - Last Name",
    "Form - Phone Number",
    "Industry",
    "Job Title",
    "Mobile Phone Number",
    "Number of Employees",
    "Personal City",
    "Personal State",
    "Personal Zip Code",
    "Phone Number",
    "Postal Code",
    "Primary Industry",
    "State (U.S.)",
    "State/Region",
]

df =  df[col]

df = df.loc[(df["Personal State"].isin(personal_state)) | (df["State/Region"].isin(state_region)) | (df['State (U.S.)'] == state_us)]
print(df.notnull().sum())
rows_count = df.count()[0]
print(f'NUM ROWS {rows_count}')
# source_of_truth 



df.to_csv('georgia.csv', mode='w')