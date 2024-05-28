
import sqlite3
import streamlit as st 
import google.generativeai as genai 
import os

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

def get_gemini_response (question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    respon = model.generate_content([prompt[0],question])
    return respon.text

def read_sql_query (sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print (row)
    return rows
        
prompt = ["""
            You are an expert in converting English questions to SQL query!
            The SQL database has the name DATA and has the following columns - NAME, CLASS, SECTION In\nFor example, \nExample 1 - How many entries of records are present?, the SQL command will be something like this SELECT COUNT(*) FROM DATA ;
            \nExample 2- Tell me all the students studying in mon2 class?, the SQL command will be something like this SELECT.* FROM DATA where CLASS="mon2";
            also the sql code should not have
            in beginning or end and sql word in output

          """]


st.set_page_config(page_title="Question")
st.header("Genmini App")
question = st.text_input("Input", key="input")
submit= st.button("Ask the question")

if submit:
   response = get_gemini_response(question, prompt)
   print(response)
   response = read_sql_query(response,"data.db")
   st.subheader("The Response is: ")
  
   for row in response:
       print(row)
       st.header(row)