import pandas as pd
import sqlite3
import xlrd

print("Start!")
file_name = '../Enodo_Skills_Assessment_Data_File.xlsx'
db_file = 'db.sqlite3'
db = sqlite3.connect(db_file)
dfs = pd.read_excel(file_name, sheet_name=None)
for table, df in dfs.items():
    df.index = df.index + 1
    df.index.names = ['id']
    df.to_sql('PropertyInfo', db)
print("Great News, Completed!")
