import sqlite3
import streamlit as st 
import google.generativeai as genai 
import os
conection = sqlite3.connect("data.db")
cursor =conection.cursor()
table_info = '''
Create table DATA(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));
'''
cursor.execute(table_info)
cursor.execute(''' Insert into DATA values ('nguyen van a','mon1','A')''')
cursor.execute(''' Insert into DATA values ('nguyen van b','mon2','A')''')
cursor.execute(''' Insert into DATA values ('nguyen van c','mon2','B')''')
cursor.execute(''' Insert into DATA values ('nguyen van d','mon3','A')''')

data = cursor.execute(''' Select * from DATA''')   
for row in data:
    print(row) 
    
conection.commit()
conection.close()





