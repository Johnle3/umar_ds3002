# %%
import pandas as pd
import requests
import json
import os
import pymysql
import mysql.connector
import sqlite3
#import sqlite - default in python now
# %%
#1.	Fetching the data by ingesting a local file on my computer:

#read the data
df = pd.read_csv('/Users/Umar/Desktop/School/UVA/Spring2022/DS3002/breast_cancer.csv')

try:    
    df_to_json = df.to_json('/Users/Umar/Desktop/School/UVA/Spring2022/DS3002/breast_cancer.json')
except:
    print("error!", df_to_json['error']['message'])
    

#view some of the data
print(df.head())
#print(data.to_string())

# %%
#2.	Converting the format of the data from CSV to JSON:
#3.	Modify the number of columns from the source to the destination:

#Here I'm removing the diagnosis column so when it converts to JSON,
#that it something that is not included. I chose this because it might be cool
#to create a cancer classification model, and to do that we shouldn't see the diagnosis.

#remove the diagnosis column
df.pop('diagnosis')

#This saves the new .json file in my directory without the diagnosis column
df.to_json ('/Users/Umar/Desktop/School/UVA/Spring2022/DS3002/breast_cancer.json')

#see that the diagnosis column is missing when we use head()
print(df.head())

# %%

#4.	Writing JSON

json_file = '/Users/Umar/Desktop/School/UVA/Spring2022/DS3002/breast_cancer.json'

with open(json_file) as f:
    data = json.load(f)

df = pd.DataFrame(data)
#print(df)

conn = sqlite3.connect('test_database')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS cancer (id, radius_mean)')
conn.commit()

df.to_sql('cancer', conn, if_exists='replace', index = False)

from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

#JSON to SQL using
#df_sql = df.to_sql(df, con=engine)
#print(df_sql)

with open('json_file', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# %%

#5.	Generate a brief summary of the data file

count_row = df.shape[0]  # Gives number of rows
print('There are ' + str(count_row) + ' rows.')

count_col = df.shape[1]  # Gives number of columns
print('There are ' + str(count_col) + ' columns.')

# %%

